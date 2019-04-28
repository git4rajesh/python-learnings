import json
import traceback

from core import utils
from core.asserter import Asserter
from core.db import db_wrapper
from entities.rollups import helper
from entities.rollups.rollups import Rollup

ENTITY = 'scope'


class Scope(Rollup):
    def __init__(self, request, parent_id, project_id):
        super().__init__(request)
        self.parent_id = parent_id
        self.project_id = project_id

    def verify_rollups(self):
        self.status = True
        self.step_desc = 'Scope Rollup verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        expected_dct = self.get_expected()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        actual_task_det_dct = self._get_actual_task_det()
        self.step_input += '\n Actual Task details rollup Dictionary\n{}'.format(json.dumps(actual_task_det_dct))

        try:
            self.status, remark = Asserter().verify(actual_task_det_dct, expected_dct=expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        assert self.status

        actual_task_heir_dct = self._get_actual_task_heir()
        self.step_input += '\n Actual Task heirarchy details rollup Dictionary\n{}'.format(
            json.dumps(actual_task_heir_dct))
        try:
            self.status, remark = Asserter().verify(actual_task_heir_dct, expected_dct=expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def get_expected(self):
        expected_dct = {'actual_hrs': 0, 'scheduled_hrs': 0, 'htc': 0.0}
        # data_store = self.data_store.get()
        leaf_tasks = helper.get_all_leaf_tasks(self.db_store, self.parent_id)
        leaf_tasks.append({'id': self.parent_id})
        tasks = leaf_tasks
        actual_hrs = 0
        for task in tasks:
            # task_dict = self.data_store.search.get_details_based_on_attributes(data_store, 'task', id=task_id)
            task_dict = self.db_store.search_by_key('task', 'id', task['id'])[0]
            if 'timesheet_row_ids' in task_dict.keys():
                for timesheet_row_id in task_dict['timesheet_row_ids']:
                    # timesheet_dict = data_store['timesheet'][timesheet_row_id]
                    timesheet_dict = self.db_store.search_by_key('timesheet', 'id', timesheet_row_id)[0]
                    for entry in timesheet_dict['entries']:
                        actual_hrs += entry['entryHours']
        expected_dct.update(actual_hrs=actual_hrs)
        return expected_dct

    def _get_actual_task_det(self):
        api = self.urls['rollup'][ENTITY]['task_det']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=self.parent_id)
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        json_resp = response.json()['data'][0]
        actual_dct = {'actual_hrs': json_resp['actualHours'], 'scheduled_hrs': json_resp['scheduledHours'],
                      'htc': float(json_resp['hoursToComplete'])}
        return actual_dct

    def _get_actual_task_heir(self):
        api = self.urls['rollup'][ENTITY]['task_heir']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            project_id=self.project_id,
            entity_id=self.parent_id)
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        json_resp = response.json()['children'][0]
        actual_dct = {'actual_hrs': json_resp['actualHours'], 'scheduled_hrs': json_resp['scheduledHours'],
                      'htc': float(json_resp['hoursToComplete'])}
        return actual_dct
