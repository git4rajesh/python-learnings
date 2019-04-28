import os
import sys
import uuid

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.logger import handler as logger
from automation.integration.src.test_case_helper import TestCaseHelper
from automation.integration.src.constants_reader import ConstantsReader
from automation.pve.controller.project import ProjectController
from automation.pve.controller.task import TaskController
from automation.pve.controller.attributes import AttributesController
from automation.pve.controller.verify import PVEVerifyController
from automation.pve.controller.teardown import PVETearDownController
from automation.integration.rally.controller.feature import FeatureController
from automation.integration.rally.controller.verify import RallyVerifyController
from automation.integration.rally.controller.teardown import RallyTearDownController
from automation.integration.base_test import TestStep
from lxml.builder import ElementMaker
from collections import OrderedDict
from automation.pve.src.constants import ATTRIBUTES


class TestStage(TestStep):
    def __init__(self, pve_env, pve_dsn, pve_db, ext_env, ext_user, integ_env, has_cert=False):
        super(TestStage, self).__init__(pve_env, pve_dsn, pve_db, ext_env, ext_user, integ_env, has_cert)

        self.id = 'PVE-76956'
        self.url = 'http://jira/browse/PVE-76956'
        self.uuid = str(uuid.uuid4())
        self.all_step_results = []

        self.project_desc = None
        self.project_key = None
        self.request_start = None
        self.request_end = None
        self.project_ctrl = ProjectController(self.id, self.uuid)
        self.task_ctrl = TaskController(self.id, self.uuid)
        self.attribute_ctrl = AttributesController(self.id, self.uuid)
        self.pve_verify_ctrl = PVEVerifyController(self.id, self.uuid)
        self.pve_tear_down_ctrl = PVETearDownController(self.id, self.uuid)
        self.rally_verify_ctrl = RallyVerifyController(self.id, self.uuid)
        self.rally_tear_down_ctrl = RallyTearDownController(self.id, self.uuid)
        self.helper = TestCaseHelper()
        self.pve_constants = ConstantsReader.get_pve_constants(pve_env, pve_dsn)

    def teardown_step(self):
        pass

    def update_step(self):
        pass

    def create_step(self):
        pass

    def verify_step(self):
        pass

    def run(self):

        self.project_desc, self.project_key, project_status = self.project_ctrl.create(self.pve_constants['father_key'])
        attribute_status = self.attribute_ctrl.set_single_attribute(self.project_key, ATTRIBUTES['PP Sync'],
                                                                     self.pve_constants['pp_sync_yes_managed_in_pve'])



        description = self.helper.get_name('MyTask')
        self.task_desc = description
        E3 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08",
                          nsmap={
                              'ns1': "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"})

        self.dict_func = OrderedDict()
        self.dict_func['E3.Description'] = (E3.Description, description)
        self.dict_func['E3.FatherKey'] = (E3.FatherKey, self.project_key)
        self.task_key, task_status = self.task_ctrl.create(self.dict_func)

        print('>> Created Task Key', self.task_key)
        print('>> Created Task Status', task_status)


        self.dict_func = OrderedDict()

        self.start_date, self.end_date = self.helper.get_date_time(0, 2)

        self.dict_func['E3.ActualFinishDate'] = (E3.ActualFinishDate, self.end_date)
        self.dict_func['E3.ActualStartDate'] = (E3.ActualStartDate, self.start_date)

        self.dict_func['E3.Description'] = (E3.Description, 'Updated Desc')
        self.dict_func['E3.EnterProgress'] = (E3.EnterProgress, 'true')
        self.dict_func['E3.FatherKey'] = (E3.FatherKey, self.project_key)
        self.dict_func['E3.Key'] = (E3.Key, self.task_key)
        # self.dict_func['E3.ScheduleFinishDate'] = (E3.ScheduleFinishDate, self.end_date)
        # self.dict_func['E3.ScheduleStartDate'] = (E3.ScheduleStartDate,self.start_date)
        self.task_key, task_status = self.task_ctrl.update(self.dict_func)

        print('>> Updated Task Key', self.task_key)
        print('>> Updated Task Status', task_status)





if __name__ == '__main__':
    args = sys.argv
    if len(args) == 8:
        pve_env = args[1]
        pve_dsn = args[2]
        pve_db = args[3]
        rally_env = args[4]
        rally_user = args[5]
        integ_env = args[6]
        run_id = args[7]
        test_obj = TestStage(pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env)
        test_obj.run()
    else:
        logger.logs('Oops! You have not provided enough parameters', 'warning')
        logger.logs('Usage python.exe tc_<id> pve_env pve_dsn pve_db rally_env rally_user integ_env', 'warning')
        sys.exit(-1)