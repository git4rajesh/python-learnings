from automation.core.logger import handler as logger
from automation.core.db.crud import Crud
from automation.core.db import db as dbo
from automation.core.src.environment import Environment
from automation.integration.src.test_case_helper import TestCaseHelper
from automation.integration.pve.model.task import Task
from automation.integration.db import query_handler as qhandler
from automation.integration.pve.db import query_handler as pve_qhandler

class TaskController:

    def __init__(self, id, uuid):
        self.task = Task()
        self.helper = TestCaseHelper()
        self.env = Environment()
        self.sql_server = self.env.pvedb.db_server
        self.sql_user = self.env.pvedb.db_user
        self.sql_pwd = self.env.pvedb.db_pwd
        self.sql_db = self.env.pvedb.db_name
        self.crud = Crud(dbo.PVEDB(self.sql_server, self.sql_user, self.sql_pwd, self.sql_db))
        self.id = id
        self.uuid = uuid
        self.list_create_task_values, self.dict_node_values = [], []

    def create(self, father_key, name='Task', encoding='utf-8'):
        logger.logs('\n Creating PVE task \n', 'info')
        description = self.helper.get_name(name)
        self.list_create_task_values = {'Description': description, 'FatherKey': father_key}
        self.task.create(self.list_create_task_values, encoding)
        task_key = self.task.verify_created_key
        status = self.verify_create(encoding)
        return description, task_key, status

    def update_old(self, task_key, father_key, milestone ='false', encoding='utf-8', **kwargs):
        logger.logs('\n Updating PVE task \n', 'info')
        update_desc = self.helper.get_name('Updated_Task')
        if milestone == 'true' and 'schedule_start' in kwargs:
            self.list_dict_node_values = [{r'ns1:Description': update_desc,
                                           r'ns1:Key': task_key,
                                           r'ns1:FatherKey': father_key,
                                           r'ns1:IsMilestone': milestone,
                                           r'ns1:ScheduleStartDate': kwargs['schedule_start'],
                                           r'ns1:EnterProgress': kwargs['enter_progress'], r'ns1:Duration': 0}]
            operation = 'update'

        else:
            if 'Actual_Finish' in kwargs and 'Actual_Start' in kwargs:
                self.list_dict_node_values = [{r'ns1:Description': update_desc,
                                               r'ns1:Key': task_key,
                                               r'ns1:FatherKey': father_key,
                                               r'ns1:IsMilestone': milestone,
                                               r'ns1:EnterProgress': kwargs['enter_progress'],
                                               r'ns1:ActualFinishDate': kwargs['Actual_Finish'],
                                               r'ns1:ActualStartDate' : kwargs['Actual_Start']}]
                operation = 'update_actual'

            elif 'Actual_Start' in kwargs and 'Schedule_start' in kwargs:
                self.list_dict_node_values = [{r'ns1:Description': update_desc,
                                               r'ns1:Key': task_key,
                                               r'ns1:FatherKey': father_key,
                                               r'ns1:EnterProgress': kwargs['enter_progress'],
                                               r'ns1:ActualStartDate' : kwargs['Actual_Start'],
                                               r'ns1:ScheduleStartDate': kwargs['Schedule_start'],
                                               r'ns1:ScheduleFinishDate' : kwargs['Schedule_Finish']}]

                operation = 'update_start_date'

            else:
                self.list_dict_node_values = [{r'ns1:Description': update_desc,
                                               r'ns1:Key': task_key,
                                               r'ns1:FatherKey': father_key,
                                               r'ns1:EnterProgress': kwargs['enter_progress'],
                                               r'ns1:ScheduleFinishDate' : kwargs['Schedule_Finish'],
                                               r'ns1:ScheduleStartDate': kwargs['Schedule_start']}]
                operation = 'update_schedule'
        self.task.update(self.list_dict_node_values, operation, encoding)
        status = self.verify_update(encoding)
        return update_desc, status

    def update(self, task_key, father_key, milestone='false', encoding='utf-8', **kwargs):
        logger.logs('\n Updating PVE task \n', 'info')
        update_desc = self.helper.get_name('Updated_Task')
        self.dict_node_values = {'Description': update_desc, 'Key': task_key, 'FatherKey': father_key,
                                 'IsMilestone': milestone}
        self.dict_node_values.update(**kwargs)
        self.task.update(self.dict_node_values, 'update', encoding)
        status = self.verify_update(encoding)
        return update_desc, status

    def read(self, planning_code):
        return pve_qhandler.select_schedule_actual_dates(planning_code, self.crud)

    def verify_create(self, encoding='utf-8'):
        logger.logs('\n Verifying the created task \n', 'info')
        result, remarks = self.task.verify_create(encoding)

        step_desc = 'Creation and Verification of the Task'
        step_input = 'Task: %s' % self.list_create_task_values

        last_run = self.helper.get_time()
        create_status = False
        step_result = 0

        if result:
            step_result = 1
            create_status = True
        qhandler.insert_into_step_details(self.id, self.uuid, self.env.pve.name, self.env.pve.db_name,
                                          self.env.external_env.name, self.env.integ.name, step_desc, step_input, step_result,
                                          remarks, last_run)
        logger.logs('Task create verification: %s' % create_status, 'info')
        return create_status

    def verify_update(self, encoding='utf-8'):
        logger.logs('\n Verifying the updated task \n', 'info')
        result, remarks = self.task.verify_update(encoding)

        step_desc = 'Update and Verification of the Task'
        step_input = 'Task: %s' % self.dict_node_values
        last_run = self.helper.get_time()
        update_status = False
        step_result = 0

        if result:
            step_result = 1
            update_status = True
        qhandler.insert_into_step_details(self.id, self.uuid, self.env.pve.name, self.env.pve.db_name,
                                          self.env.external_env.name, self.env.integ.name, step_desc, step_input, step_result,
                                          remarks, last_run)
        logger.logs('Task update verification: %s' % update_status, 'info')
        return update_status
