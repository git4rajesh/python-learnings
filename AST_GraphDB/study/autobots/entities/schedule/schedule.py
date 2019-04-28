import json
import traceback

from core.asserter import Asserter
from core.db import db_wrapper
from entities.schedule.base import Base
from entities.timesheet.timesheet import Timesheet

ENTITY = 'schedule'

class Schedule(Base):
    def __init__(self, request):
        super().__init__(request)
        self.task_id = None
        self.project_id = None
        self.asserter = Asserter()

    def add_resource(self, resource_name, role_name):
        """
        Atom is to add resource to the schedule
        :param resource_name: name of the resource example : 'ba_user' or 'project_owner1'
        :param role_name: role names which is to betaken from the constants example : 'ba' or 'architect'
        """
        data = {'role_id': self.constants['ROLES'][role_name]['ID'],
                'resource_id': self.constants['USERS'][resource_name]['RESOURCEID'], 'task_id': self.task_id}
        self.task_role_id, self.resource_task_schedule_id = super().create(**data)
        return self

    def set_role_hrs(self, estimated_hrs):
        """
        This is to estimate the hours for a role which is assigned to the task
        :param estimated_hrs: estimated hrs in integer
        """
        data = {'task_role_id': self.task_role_id, 'task_id': self.task_id, 'estimated_hrs': estimated_hrs}
        super().update(**data)
        return self

    def set_resource_hrs(self, resource_hrs, resource_htc=0):
        """
        This is set resource hours and hours to complete for a particular role and its task id
        :param resource_hrs: resource hrs in integer
        :param resource_htc: resource hts in integer
        """
        data = {'payload': 'resource_hrs', 'resource_task_schedule_id': self.resource_task_schedule_id,
                'task_role_id': self.task_role_id,
                'task_id': self.task_id, 'resource_hrs': resource_hrs, 'resource_htc': resource_htc}
        super().update(**data)
        return self

    def delete(self, entity_details):
        pass

    def timesheet(self):
        """
        The time sheet object is created, which defines a relationship between schedule and timesheet
        :return: timesheet object
        """
        obj = Timesheet(self.request)
        obj.project_id = self.project_id
        obj.task_id = self.task_id
        return obj

    def verify(self):
        """
        This mehod will generate expected dict from the data store and
        actual dict is generated from read operation of the project entity
        :return: status
        """
        self.status = True
        self.step_desc = 'Task update verification'
        from core import utils
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        expected_dct = self.db_store.search_by_key(ENTITY, 'taskRoleId', str(self.task_role_id))[0]
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        response = super().read(entity_id=self.task_id)
        actual_dct = utils.get_sub_dct(response, expected_dct)
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))

        try:
            self.status, remark = self.asserter.verify(actual_dct, expected_dct=expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        assert self.status
        return self
