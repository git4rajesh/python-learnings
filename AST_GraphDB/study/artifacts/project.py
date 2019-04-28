import json
import traceback
from core.db import db_wrapper
from entities.issue.issue import Issue

from entities.project.base import Base
from entities.task.task import Task
from core.asserter import Asserter
from core import utils

ENTITY = 'project'


class Project(Base):
    def __init__(self, request):
        super().__init__(request)
        self.asserter = Asserter()

    def create(self, title=None, template=None):
        """
        project can be created with or without template
        :param template:  template_id
        :return: self object
        """
        data = {'title': title}
        if template:
            data = {'payload': 'template', 'template': template}
        super().create(**data)
        return self

    def _update(self, **data):
        """
        Atom to update the attributes for the given project_id
        :param data: data wil have attributes which needs to be updated from the atoms
        :return: self object
        """
        data.update(entity_id=self.project_id)
        super().update(**data)
        return self

    def delete(self, entity_details=None):
        """
        Atom to delete the project which calls base delete
        :return: self object
        """
        if not entity_details:
            entity_id = self.project_id
        else:
            entity_id = entity_details['id']
        super().delete(entity_id=entity_id)
        return self

    def set_title(self, title):
        """
        Atom to update the title of the project
        :param title: title which needs to be updated for the given project
        :return: self object
        """
        self._update(payload='title', title=title)
        return self

    def set_owner(self, owner):
        """
        Atom to set the owner for the given project id
        :param owner: owner which needs to be set as owner of the project
        :return: self object
        """
        self._update(payload='owner',
                     owner_id=self.constants['USERS'][owner]['RESOURCEID'],
                     owner_value=self.constants['USERS'][owner][
                         'DISPLAYTEXT'])
        return self

    def set_description(self, description):
        """
        Atom to update the description
        :param description: description
        :return: self object
        """
        self._update(payload='description', description=description)
        return self

    def set_confidential(self, is_confidential_value):
        """
        Atom to update the below param attributes for the given project
        :param is_confidential_id:
        :param is_confidential_value:
        :return: self object
        """
        confidential_dct = {'yes': 1, 'no': 0}
        is_confidential_id = confidential_dct.get(is_confidential_value.lower())
        self._update(payload='confidential',
                     is_confidential_id=is_confidential_id,
                     is_confidential_value=is_confidential_value)
        return self

    def set_phase(self, phase):
        self._update(payload='phase',
                     phase_id=self.constants['PROJECT']['PHASES'][phase]['ID'],
                     phase_value=self.constants['PROJECT']['PHASES'][phase]['DISPLAYTEXT'])
        return self

    def set_complete_date(self, complete_date_time):
        """
        set complete date for the project
        :param complete_date_time: complete date in yyyy-mm-ddT00:00:00.000 format
        """
        self._update(payload='completed_date',
                     complete_date_time=complete_date_time)
        return self

    def set_status(self, status):
        """
        set status for the project, as per the input given it will
        get the id for the status and appends it to the payload
        :param status: status like 'proposed' or 'Hold'
        """
        self._update(payload='status',
                     status_id=self.constants['PROJECT']['STATUS'][status]['ID'],
                     status_value=self.constants['PROJECT']['STATUS'][status]['DISPLAYTEXT'])
        return self

    def set_department(self, department):
        """
        set department for the project, as per the input given it will
        get the id for the department and appends it to the payload
        :param department: department like 'customer' or 'Finance'
        """
        self._update(payload='department',
                     department_id=self.constants['PROGRAMS'][department][
                         'ID'],
                     department_value=self.constants['PROGRAMS'][department]['DISPLAYTEXT'])
        return self

    def task(self, title, type='noncap_nonbill'):
        """
        Task is created, which defines a relationship between project and task
        :param title:
        :param type:
        :return:
        """
        obj = Task(self.request).create_under_project(title, type,
                                                      project_id=self.project_id)
        return obj

    def multipletasks(self, title_lst):
        """
        Purpose of this function is to create a list of tasks
        """
        obj = Task(self.request)._multipletasks(title_lst)
        return obj

    def issue(self, title):
        obj = Issue(self.request).create(title)
        return obj

    def verify(self):
        """
        This mehod will generate expected dict from the data store and
        actual dict is generated from read operation of the project entity
        :return: status
        """
        self.status = True
        self.step_desc = 'Project update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        expected_dct = self.db_store.search_by_key(ENTITY, 'id', self.project_id)[0]
        title = expected_dct.get('title')
        encoded_title = utils.html_encode(title)
        expected_dct.update({'title': encoded_title})
        if expected_dct.get('description'):
            description = expected_dct.get('description')
            encoded_desc = utils.html_encode(description)
            expected_dct.update({'description': encoded_desc})
        self.step_input = json.dumps(expected_dct)

        response = super().read(entity_id=self.project_id)
        actual_dct = response.json()['data'][0]

        try:
            self.status, remark = self.asserter.verify(actual_dct,
                                                       expected_dct=expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        assert self.status
        return self
