import os
import sys
import uuid
import traceback

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.logger import handler as logger
from automation.integration.src.test_case_helper import TestCaseHelper
from automation.integration.src.constants_reader import ConstantsReader
from automation.integration.pve.controller.project import ProjectController
from automation.integration.pve.controller.task import TaskController
from automation.integration.base_test import TestStep

__author__ = 'Shalini'

class TestCase(TestStep):
    """
    Test Jinja Template for TASK artifact
    """

    def __init__(self, pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env, has_cert=False):
        super(TestCase, self).__init__(pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env, has_cert)

        self.type = 'Regression'
        self.id = 'Test-Jinja'
        self.url = 'http://jira/browse/'
        self.uuid = str(uuid.uuid4())
        self.all_step_results = []

        self.project_ctrl = ProjectController(self.id, self.uuid)
        self.task_ctrl = TaskController(self.id, self.uuid)
        self.helper = TestCaseHelper()

        self.pve_constants = ConstantsReader.get_pve_constants(pve_env, pve_dsn)

    def create_step(self):
        self.project_desc, self.project_key, project_status = self.project_ctrl.create(self.pve_constants['father_key'])
        self.task_desc, self.task_key, task_status = self.task_ctrl.create(self.project_key)
        self.all_step_results.extend([task_status, self.project_desc, self.project_key, self.task_key, self.task_desc ])

    def update_step(self):
        update_desc, task_status = self.task_ctrl.update(self.task_key, self.project_key,
                                                         ScheduleStartDate='2017-03-21T15:20:00',
                                                         EnterProgress='true')
        self.all_step_results.extend([update_desc, task_status])

    def verify_step(self):
        pass

    def teardown_step(self):
        pass

    def run(self, run_id):
        logger.logs('Running Test case %s' % self.id, 'info')
        logger.logs('Description for the Test case %s' % self.__doc__, 'info')

        try:
            self.create_step()
            self.update_step()


        except:
            logger.logs('!!! EXCEPTION OCCURRED in Test Case: %s run method. Please troubleshoot !!!' % self.id, 'error')
            logger.logs('Exception Trace: \n %s', traceback.print_exc())
            self.all_step_results.append(False)
        finally:
            test_result = all(self.all_step_results)
            # self.finalize_step(self.id, self.uuid, test_result, run_id)


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
        test_obj = TestCase(pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env)

        test_obj.run(run_id)
    else:
        logger.logs('Oops! You have not provided enough parameters', 'warning')
        logger.logs('Usage python.exe tc_<id> pve_env pve_db rally_env integ_env', 'warning')
        sys.exit(-1)