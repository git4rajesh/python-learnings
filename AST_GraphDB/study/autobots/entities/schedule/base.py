import json

from core import utils
from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.entity import Entity

ENTITY = 'schedule'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.ttl = request.scope
        self.payload_generator.request = request

    @payload_generator.generate_payload
    def create(self, **data):
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            task_id=data['task_id'])

        payload = data['payload']
        response = self.rqst_session.post(url, json=payload, cookies={'JSESSIONID': self.jsessionid})
        taskRoleId, resourceTaskScheduleId = self.verify_create(response)
        self.db_store.insert(self.scope, self.test_id, ENTITY, response.json())
        return taskRoleId, resourceTaskScheduleId

    def read(self, **data):
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            task_id=data['entity_id'])
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        return response

    @payload_generator.generate_payload
    def update(self, **data):
        api = self.urls[ENTITY]['update']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            task_id=data['task_id'])
        payload = data['payload']
        response = self.rqst_session.put(url, json=payload, cookies={'JSESSIONID': self.jsessionid})
        self.verify_update(response)
        self.db_store.update_by_key(ENTITY, 'taskRoleId', data['task_role_id'], payload['data'])

    def delete(self, **data):
        pass

    def verify_create(self, response):
        self.status = True
        self.step_desc = 'Innotas  Schedule verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        taskRoleId = ''
        resourceTaskScheduleId = ''

        if response.status_code == 200:
            taskRoleId = response.json()['taskRoles'][1]['taskRoleId']
            resourceTaskScheduleId = response.json()['taskRoles'][1]['resourceTaskScheduleId']
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return taskRoleId, resourceTaskScheduleId

    def verify_update(self, response):
        self.status = True
        self.step_desc = 'schedule update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        if response.status_code == 200:
            self.remarks += 'schedule updated successfully'
        else:
            self.status = False
            self.remarks += 'schedule updation failed : {}'.format(response.text)
        db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def verify_delete(self, response, artifact_id, ttl):
        pass
