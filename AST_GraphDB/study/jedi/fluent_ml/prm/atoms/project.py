from automation.core.datastore.tinydb_datastore import DataStore
from automation.integration.src.time_testcase_helper import TimeTestCaseHelper
from automation.fluent_ml.prm.features.attribute import Attribute
from automation.fluent_ml.prm.atoms.artifact import PRM
from automation.fluent_ml.prm.features.prm_verify import PRMVerify
from automation.fluent_ml.prm.features.project import Project
from automation.fluent_ml.src import helper
from automation.pve.src.constants import ATTRIBUTES


# def get_project_scode(table_name, name):
#     project_details = DataStore.read(table_name, name=name)
#     project_key = project_details['id']
#     scode = helper.get_scode(project_key)
#     return scode


class ProjectAtom(PRM):

    def __init__(self, name=None, lk_flag=False):
        super().__init__()
        self.initialize()
        self.father_key = self.prm_constants['father_key']
        self.project_key = self._get_project_id(name, lk_flag)

    def initialize(self):
        self.payload_update = []
        self.project = Project()
        self.table_name = self.project.tbl_name
        self.attribute = Attribute()
        self.prm_verify = PRMVerify()
        self.lst_payload = []

    def _get_project_id(self, name, lk_flag):
        if name:
            project_details = DataStore.read(self.table_name, name=name)
            if project_details:
                project_key = project_details['id']
            else:
                project_key = self.create(name, lk_flag)
            return project_key

    def goto_project(self, name):
        project_details = DataStore.read(self.table_name, name=name)
        self.project_key = project_details['id']
        return self

    def create(self, name, lk_flag):
        project_key = None
        project_details = DataStore.read(self.table_name, name=name)

        if not project_details:
            payload_create = {'FatherKey': self.father_key, 'Description': name}
            project_key = self.project.create(payload_create)

            if lk_flag:
                self._set_lk_flag(project_key)

        return project_key

    def create_with_description(self, name, description, lk_flag=False):
        project_details = DataStore.read(self.table_name, name=name)

        if not project_details:
            payload_create = {'FatherKey': self.father_key, 'Description': name}
            self.project_key = self.project.create(payload_create)
            self.update_description(description)

            if lk_flag:
                self._set_lk_flag(self.project_key)

        return self

    def create_multiple_projects(self, lst_project_names, lk_flag=False):

        for prj_name in lst_project_names:
            payload_create = {'FatherKey': self.father_key, 'Description': prj_name}
            project_key = self.project.create(payload_create)

            if lk_flag:
                self._set_lk_flag(project_key)
        return self

    def update(self):
        # project_details = DataStore.read(self.table_name, name=name)
        project_key = self.project_key

        for dct_payload in self.lst_payload:
            dct_payload.update({'EntityKey': project_key})
        self.attribute.set(self.lst_payload)
        return self

    def update_description(self, work_description):
        project_key = self.project_key

        dct_payload = {'EntityKey': project_key, 'DeleteValue': 'false', 'Id': ATTRIBUTES['Work Description'],
                       'Value': work_description}
        lst_payload = [dct_payload]
        self.attribute.set(lst_payload)
        return self

    def update_name(self, name):
        project_key = self.project_key

        dct_payload = {'EntityKey': project_key, 'DeleteValue': 'false', 'Id': ATTRIBUTES['Description'],
                       'Value': name}
        lst_payload = [dct_payload]
        self.attribute.set(lst_payload)
        return self

    def update_scheduled_start_and_finish(self, scheduled_start, scheduled_finish):
        project_key = self.project_key
        project_details = DataStore.read(self.table_name, id=project_key)
        name = project_details['name']

        payload_update = {'Key': project_key, 'Description': name, 'FatherKey': self.father_key,
                          'ScheduleStartDate': scheduled_start, 'ScheduleFinishDate': scheduled_finish}
        self.project.update(payload_update)
        return self

    def delete(self):
        project_key = self.project_key

        setattr(ProjectAtom, 'deleted_project_key', project_key)
        self.project.delete(project_key)
        return self

    def _set_lk_flag(self, project_key):
        value = self.prm_constants['lk_sync_yes']

        dct_payload = {'EntityKey': project_key, 'DeleteValue': 'false', 'Id': ATTRIBUTES['LK Sync'], 'Value': value}
        lst_payload = [dct_payload]
        self.attribute.set(lst_payload)
        return self

    def verify_lk_url(self):
        scode = helper.get_scode(self.project_key)

        ext_env = self.env.external_env
        protocol = ext_env.protocol
        env_name = ext_env.name
        prm_env_id = self.prm_constants['prm_environment_id']

        url = '{0}://{1}/card/external/enterpriseone/{2}/{3}'.format(protocol, env_name, scode, prm_env_id)
        dct_expected = {'LK_CARD_LINK_URL': url}

        self.prm_verify.project_details(scode, dct_expected)

        return self

    def verify_lk_total_cards(self, total_no_of_cards):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_TOTAL': total_no_of_cards}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_not_started_child_cards(self, no_of_not_started_cards):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_NOT_STARTED': no_of_not_started_cards}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_in_process_child_cards(self, no_of_in_progress_cards):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_IN_PROGRESS': no_of_in_progress_cards}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_completed_child_cards(self, no_of_completed_cards):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_COMPLETE': no_of_completed_cards}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_percent_of_cards_completed(self, percent_of_cards_completed):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_PCT_CMPLT': percent_of_cards_completed}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_top_lane(self, lane_name):
        top_lane = self.prm_constants['lk_top_lane']
        l_name = top_lane[lane_name]
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_TOP_LANE': l_name}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_card_lane_status(self, lane_class_status):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_LANE_CLASS': lane_class_status}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_default_lk_top_lane(self):
        top_lane = self.prm_constants['default_lane_mapping']
        l_name = top_lane['name']
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_TOP_LANE': l_name}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_default_lk_card_lane_status(self):
        top_lane = self.prm_constants['default_lane_mapping']
        class_status = top_lane['class_status']
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_LANE_CLASS': class_status}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_earliest_actual_start(self):
        project_details = DataStore.read(self.table_name, id=self.project_key)
        name = project_details['name']

        from automation.fluent_ml.leankit.atoms.card import CardAtom
        card_obj = CardAtom()
        earliest_actual_start = card_obj.get_earliest_actual_start(name)
        prm_date_format = TimeTestCaseHelper.date_formatter_prm(earliest_actual_start)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_EARLIEST_ACT_STRT': prm_date_format}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_latest_actual_finish(self):
        project_details = DataStore.read(self.table_name, id=self.project_key)
        name = project_details['name']

        from automation.fluent_ml.leankit.atoms.card import CardAtom
        card_obj = CardAtom()
        latest_actual_finish = card_obj.get_latest_actual_finish(name)
        prm_date_format = TimeTestCaseHelper.date_formatter_prm(latest_actual_finish)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_LATEST_ACT_FINISH': prm_date_format}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_earliest_planned_start(self, earliest_planned_start):
        expected_planned_date = TimeTestCaseHelper.date_formatter_prm(earliest_planned_start)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_EARLIEST_PLN_STRT': expected_planned_date}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_latest_planned_finish(self, latest_planned_finish):
        expected_planned_date = TimeTestCaseHelper.date_formatter_prm(latest_planned_finish)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_LATEST_PLN_FINISH': expected_planned_date}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_planned_start(self, planned_start):
        expected_planned_date = TimeTestCaseHelper.date_formatter_prm(planned_start)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_PLANNED_START': expected_planned_date}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_planned_finish(self, planned_finish):
        expected_planned_date = TimeTestCaseHelper.date_formatter_prm(planned_finish)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_PLANNED_FINISH': expected_planned_date}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_actual_start(self):
        from automation.fluent_ml.leankit.atoms.card import CardAtom
        card_obj = CardAtom()

        project_details = DataStore.read(self.table_name, id=self.project_key)
        name = project_details['name']

        actual_start = card_obj.get_actual_start(name)
        formatted_actual_start = TimeTestCaseHelper.date_formatter_prm(actual_start)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_ACTUAL_START': formatted_actual_start}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_actual_finish(self):
        from automation.fluent_ml.leankit.atoms.card import CardAtom
        card_obj = CardAtom()

        project_details = DataStore.read(self.table_name, id=self.project_key)
        name = project_details['name']

        actual_finish = card_obj.get_actual_finish(name)
        formatted_actual_finish = TimeTestCaseHelper.date_formatter_prm(actual_finish)

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_ACTUAL_FINISH': formatted_actual_finish}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_priority(self, priority):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_PRIORITY': priority}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_blocked_flag(self, blocked_flag):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_IS_BLOCKED': blocked_flag}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_missed_start_child_cards(self, exception_count):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_MISSED_START': exception_count}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_missed_finish_child_cards(self, exception_count):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_MISSED_FIN': exception_count}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_blocked_child_cards(self, blocked_card_count):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_BLOCKED': blocked_card_count}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_exception_count(self, exception_count):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_EXCEPTIONS': exception_count}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_exception_percent(self, exception_percent):
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CRDS_EXCEPT_PCT': exception_percent}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_description(self, description):
        scode = helper.get_scode(self.project_key)
        self.prm_verify.project_description(scode, description)
        return self

    def exists(self):
        scode = helper.get_scode(self.project_key)
        project_details = DataStore.read(self.table_name, id=self.project_key)
        name = project_details['name']

        self.prm_verify.project_name(scode, name)
        return self

    def not_exists(self):
        project_key = getattr(ProjectAtom, 'deleted_project_key')
        self.project.verify_delete(project_key)
        return self

    def verify_lk_card_type(self, card_type='default'):
        card_type = self.prm_constants['lk_card_type'][card_type]
        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CARD_TYPE': card_type}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_lk_card_text(self):
        project_details = DataStore.read(self.table_name, id=self.project_key)
        card_id = project_details['external_id']

        scode = helper.get_scode(self.project_key)
        dct_expected = {'LK_CARD_LINK_TXT': card_id}
        self.prm_verify.project_details(scode, dct_expected)
        return self

    def verify_name(self, name):
        scode = helper.get_scode(self.project_key)
        self.prm_verify.project_name(scode, name)
        return self

    def verify_truncated_name(self, truncated_name):
        scode = helper.get_scode(self.project_key)
        self.prm_verify.project_name(scode, truncated_name)
        return self

    def teardown(self, scope):
        lst_record = DataStore.read_by_scope(self.table_name, scope=scope)

        for record in lst_record:
            project_key = record['id']
            self.project.delete(project_key)

        return self
