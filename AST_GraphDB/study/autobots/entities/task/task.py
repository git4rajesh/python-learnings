import json
import traceback

from core import utils
from core.db import db_wrapper
from entities.schedule.schedule import Schedule
from entities.task.base import Base
from entities.timesheet.timesheet import Timesheet
from core.asserter import Asserter

ENTITY = 'task'


class Task(Base):
    def __init__(self, request):
        super().__init__(request)
        self.asserter = Asserter()

    def create(self, title, type):
        """
        Atom to create the task under a project
        :param title: title of the task
        :param type: type of the tests (cap_bill, noncap_bill, noncap_nonbill, cap_nonbill)
        """
        self.create_under_project(title, type)
        return self

    def create_under_project(self, title, type, **data):
        """
        Atom to create under the project/summary task,
        type will decide which kind of the test it should be
        :param title: title of the task
        :param type: type of the tests (cap_bill, noncap_bill, noncap_nonbill, cap_nonbill)
        :param data: other optional params
        :return: self object
        """
        data.update(project_id=data.get('project_id', self.project_id))
        super().create(**data)
        self._update(title=title, payload=type)
        return self

    def _multipletasks(self, task_lst):
        """
        Atom for creating multiple tasks and store store at a stretch
        :param task_lst: list of dict with names and type
                        [{'title':<<title1>, 'type':cap_bill}, {'title':<<title2>>, 'type':noncap_bill}....]
        :return: self object
        """
        for task in task_lst:
            self.create_under_project(task.get('title'), task.get('type', 'noncap_nonbill'), project_id=self.project_id)
        return self

    def childtask(self, title=None, parent=None, **data):
        """
        Atom to create a child task under a summary task
        :param title: title, if title is not given then it will auto generate the title
        :param parent: name of the summary task under which child task has to be created
        :param data: other params if any
        :return: self object
        """
        if parent:
            task_dict = self._get_task(parent)
            self.task_id = task_dict['id']
            self.project_id = task_dict['projectId']['value']
        data.update(parent_type='task', payload='default_subtask', task_id=self.task_id,
                    project_id=self.project_id)
        super().create(**data)
        # self._set_task_details()
        if title:
            self.set_title(title)
        return self

    def _get_task(self, title):
        # task_dict = self.db.search.get_details_based_on_attributes(self.data_store.get(), ENTITY, title=title)
        task_dict = self.db_store.search_by_key(ENTITY, 'title', title)[0]
        return task_dict

    def _update(self, **data):
        data.update(task_id=self.task_id, project_id=self.project_id)
        super().update(**data)
        return self

    def set_predecessor(self, predecessor_task_titles):
        """
        Atom to set predecessor for the given tasks
        :param predecessor_task_titles: list of titles which needs to be set as predecessor ['title1', 'title2']
        :return: self object
        """
        lst_task_numbers = []
        from payloads.task.update import predecessor_dct
        tsk_dict = {}
        for predecessor_task_title in predecessor_task_titles:
            predecessor_obj = self._get_task(predecessor_task_title)
            tsk_dict[predecessor_obj.task_id] = predecessor_obj.task_number
            lst_task_numbers.append(predecessor_obj.task_number)
        data = {'payload': 'predecessor', 'task_id': self.task_id, 'project_id': self.project_id,
                'predecessor_dct': predecessor_dct, 'tsk_dict': tsk_dict}
        self._update(**data)
        return self

    def set_successor(self, successor_task_titles):
        """
        Atom to set successor for the given tasks
        :param successor_task_titles: list of titles which needs to be set as successor ['title1', 'title2']
        :return: self object
        """
        lst_task_numbers = []
        from payloads.task.update import successor_dct
        tsk_dict = {}
        for successor_task_title in successor_task_titles:
            successor_obj = self._get_task(successor_task_title)
            tsk_dict[successor_obj.task_id] = successor_obj.task_number
            lst_task_numbers.append(successor_obj.task_number)
        data = {'payload': 'successor', 'task_id': self.task_id, 'project_id': self.project_id,
                'successor_dct': successor_dct, 'tsk_dict': tsk_dict}
        self._update(**data)
        return self

    def set_title(self, title):
        """
        Atom to update the title of the task
        :param title: title of the task
        :return: self object
        """
        self._update(payload='title', title=title)
        return self

    def set_description(self, description):
        """
        Atom to updatet he description of the task
        :param description: description
        :return: self object
        """
        self._update(payload='description', description=description)
        return self

    def set_status(self, status):
        """
        Atom to update the status of the task
        :param status_id: id for the status like '858147044'
        :param status_value: value for the status like 'Approved - Not Started'
        :return: self object
        """
        self._update(payload='status', status_id=self.constants['TASK']['STATUS'][status]['ID'],
                     status_value=self.constants['TASK']['STATUS'][status]['DISPLAYTEXT'])
        return self

    def set_duration(self, days_in_sec):
        """
        Atom to update the duration of the task
        :param days_in_sec: days in seconds like 28800 (60 * 60 * 8) for one working day of 8 workings hrs
        :return:
        """
        self._update(payload='duration', duration=days_in_sec)
        return self

    def set_start_date(self, start_date_time):
        """
        Atom to update the start date of the task
        :param start_date_time: date should be of datetime format of '%Y-%m-%dT%H:%M:%S.000'
        :return: self object
        """
        self._update(payload='start_date', start_date_time=start_date_time)
        return self

    def set_complete_date(self, complete_date_time):
        """
        Atom to update the complete date of the task
        :param complete_date_time: date should be of datetime format of '%Y-%m-%dT%H:%M:%S.000'
        :return: self object
        """
        self._update(payload='completed_date', complete_date_time=complete_date_time)
        return self

    def delete(self, entity_details=None):
        if not entity_details:
            entity_id = self.task_id
        else:
            entity_id = entity_details['id']
        super().delete(entity_id=entity_id)
        return self

    def schedule(self):
        """
        This method is used to create the object of schedule class,
        which defines a relationship between schedule and timesheet
        :return: schedule object
        """
        obj = Schedule(self.request)
        obj.task_id = self.task_id
        obj.project_id = self.project_id
        return obj

    def timesheet(self):
        """
        This method is used to create the object of timesheet class,
        which defines a relationship between schedule and timesheet
        :return: timesheet object
        """
        obj = Timesheet(self.request)
        obj.project_id = self.project_id
        obj.task_id = self.task_id
        return obj

    def verify(self):
        """
        This mehod will generate expected dict from the data store and
        actual dict is generated from read operation of the task entity
        :return: status
        """
        self.status = True
        self.step_desc = 'Task update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        expected_dct = self.db_store.search_by_key(ENTITY, 'id', self.task_id)[0]
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))

        title = expected_dct.get('title')
        encoded_title = utils.html_encode(title)
        expected_dct.update({'title': encoded_title})
        if expected_dct.get('description'):
            description = expected_dct.get('description')
            encoded_desc = utils.html_encode(description)
            expected_dct.update({'description': encoded_desc})
        self.step_input = json.dumps(expected_dct)
        response = super().read(entity_id=self.task_id)
        actual_dct = response.json()['data'][0]
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
