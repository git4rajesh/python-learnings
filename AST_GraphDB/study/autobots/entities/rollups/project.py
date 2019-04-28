import json
import traceback

from core import utils
from core.db import db_wrapper
from entities.rollups import helper
from entities.rollups.rollups import Rollup
from core.asserter import Asserter
from entities.user.rate.rate import Rate

ENTITY = 'project'


class Project(Rollup):
    def __init__(self, request, project_id):
        super().__init__(request)
        self.request = request
        self.project_id = project_id
        self._initialize_expected_dict()

    def verify_rollups(self):
        self.status = True
        self.step_desc = 'Project Rollup verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        expected_dct = self.get_expected()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        actual_dct = self.get_actual()
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))

        try:
            self.status, remark = Asserter().verify(actual_dct, expected_dct=expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def get_expected(self):
        expected_dct = {}
        tasks = helper.get_all_leaf_tasks(self.db_store, self.project_id)
        for task in tasks:
            task_dict = self.db_store.search_by_key('task', 'id', task['id'])[0]
            if 'timesheet_row_ids' in task_dict.keys():
                for timesheet_row_id in task_dict['timesheet_row_ids']:
                    timesheet_dict = self.db_store.search_by_key('timesheet', 'id', timesheet_row_id)[0]
                    self._calc_expected(timesheet_dict)

        self._calc_total_dct()
        self._calc_profit_margin_dct()

        expected_dct.update(**self.billable_dct, **self.non_billable_dct,
                            **self.capitalized_dct, **self.non_capitalized_dct,
                            **self.total_dct, **self.profit_margin_dct)
        return expected_dct

    def get_actual(self):
        api = self.urls['rollup'][ENTITY]
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            project_id=self.project_id)
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid}, headers={
            'X-Requested-With': 'XMLHttpRequest'})
        actual_dct = helper.parse_to_dict(response.content)
        return actual_dct

    def _initialize_expected_dict(self):
        inner_dct = {'estimated': 0.0, 'actual': 0.0, '% recognized': 0.0,
                     'variance': 0.0}
        self.billable_dct = {'Billable Hrs': inner_dct.copy(),
                             'Billable Cost': inner_dct.copy(),
                             'Revenue': inner_dct.copy()}
        self.non_billable_dct = {'Non Billable Hrs': inner_dct.copy(),
                                 'Non Billable Cost': inner_dct.copy(),
                                 'Non Billable Amount': inner_dct.copy()}
        self.capitalized_dct = {'Capitalized Cost': inner_dct.copy()}
        self.non_capitalized_dct = {'Non-Capitalized Cost': inner_dct.copy()}
        self.total_dct = {'Total Cost': inner_dct.copy(),
                          'Total Hours': inner_dct.copy()}
        self.profit_margin_dct = {'Profit': inner_dct.copy(),
                                  'Margin': inner_dct.copy()}

    def _calc_expected(self, task_timesheet_dct):
        for entry in task_timesheet_dct['entries']:
            hours = entry['entryHours']
            rate = float(entry['internalRate'])
            self._calc_billable_dct(task_timesheet_dct, hours, rate)
            self._calc_non_billable_dct(task_timesheet_dct, hours, rate)
            self._calc_capitalized_dct(task_timesheet_dct, hours, rate)
            self._calc_non_capitalized_dct(task_timesheet_dct, hours, rate)

    def _calc_billable_dct(self, task_timesheet_dct, hours, rate):
        if task_timesheet_dct['isBillable']:
            bill_hrs = self.billable_dct['Billable Hrs']
            bill_hrs['actual'] += hours
            bill_hrs['variance'] = bill_hrs['estimated'] - bill_hrs['actual']

            bill_cost = self.billable_dct['Billable Cost']
            bill_cost['actual'] += hours * rate
            bill_cost['variance'] = bill_cost['estimated'] - bill_cost['actual']

            self.billable_dct['Revenue']['actual'] = 0

    def _calc_non_billable_dct(self, task_timesheet_dct, hours, rate):
        if not task_timesheet_dct['isBillable']:
            nonbill_hrs = self.non_billable_dct['Non Billable Hrs']
            nonbill_hrs['actual'] += hours
            nonbill_hrs['variance'] = nonbill_hrs['estimated'] - nonbill_hrs[
                'actual']

            nonbill_cost = self.non_billable_dct['Non Billable Cost']
            nonbill_cost['actual'] += hours * rate
            nonbill_cost['variance'] = nonbill_cost['estimated'] - nonbill_cost[
                'actual']

            self.non_billable_dct['Non Billable Amount']['actual'] = 0

    def _calc_capitalized_dct(self, task_timesheet_dct, hours, rate):
        if task_timesheet_dct['isCapitalized']:
            cap_cost = self.capitalized_dct['Capitalized Cost']
            cap_cost['actual'] += hours * rate
            cap_cost['variance'] = cap_cost['estimated'] - cap_cost['actual']

    def _calc_non_capitalized_dct(self, task_timesheet_dct, hours, rate):
        if not task_timesheet_dct['isCapitalized']:
            noncap_cost = self.non_capitalized_dct['Non-Capitalized Cost']
            noncap_cost['actual'] += hours * rate
            noncap_cost['variance'] = noncap_cost['estimated'] - noncap_cost[
                'actual']

    def _calc_total_dct(self):
        total_cost = self.total_dct['Total Cost']
        total_cost['actual'] = self.billable_dct['Billable Cost']['actual'] + \
                               self.non_billable_dct['Non Billable Cost'][
                                   'actual']
        total_cost['variance'] = total_cost['estimated'] - total_cost[
            'actual']

        total_hrs = self.total_dct['Total Hours']
        total_hrs['actual'] = self.billable_dct['Billable Hrs']['actual'] + \
                              self.non_billable_dct['Non Billable Hrs'][
                                  'actual']
        total_hrs['variance'] = total_hrs['estimated'] - total_hrs[
            'actual']

    def _calc_profit_margin_dct(self):
        profit = self.profit_margin_dct['Profit']
        profit['actual'] = \
            self.billable_dct['Revenue']['actual'] - \
            self.total_dct['Total Cost']['actual']
        profit['variance'] = profit['estimated'] - profit[
            'actual']
