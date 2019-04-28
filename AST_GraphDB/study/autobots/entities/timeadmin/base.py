import json

from core import utils
from core.db import db_wrapper
from entities.entity import Entity
from core.src.json_generator import PayloadGenerator

ENTITY = 'timesheet'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.project_id = None
        self.task_id = None
        self.ttl = request.scope
        self.payload_generator.request = request

    def create(self):
        pass

    @payload_generator.generate_payload
    def update(self, **data):
        payload = data['payload']
        api = self.urls['timesheet']['update']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env']
        )
        url = '{url}/{timesheet_id}/activities?mgr=true'.format(url=url, timesheet_id=data['timesheet_id'])
        response = self.rqst_session.put(url, json=payload, cookies={
            'JSESSIONID': self.jsessionid})
        self.verify_update(response)
        # self._add_timesheet_to_store(read_response, data['task_id'], timesheet_id)

    def read(self, **data):
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            timesheet_id=data['entity_id'])
        url = '{url}?mgr=true'.format(url=url)
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def delete(self, *args, **kwargs):
        pass

    def verify_create(self, *args, **kwargs):
        pass

    def verify_update(self, response):
        """
        verification of the response after the update on user rate in timesheet by timeadmin entity
        for the given timesheet row on a specific day and specific task
        :param response: response after update call
        """
        self.status = True
        self.step_desc = 'Timeadmin updation of user rate in timesheet - verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)

        if response.status_code == 200:
            self.remarks += 'Timeadmin updated successfully'
        else:
            self.status = False
            self.remarks += 'Timeadmin updation of user rate in timesheet failed : {}'.format(response.text)
        db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def verify_delete(self, *args, **kwargs):
        pass
