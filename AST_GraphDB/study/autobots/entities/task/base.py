import json

from core import utils
from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.entity import Entity
from entities.task.helper import construct_subsection_lst

ENTITY = 'task'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.project_id = None
        self.task_id = None
        self.ttl = request.scope
        self.payload_generator.request = request
        self.payload_generator.env.globals.update(
            construct_lst=construct_subsection_lst)

    @payload_generator.get_parent_id
    @payload_generator.generate_payload
    def create(self, **data):
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'])

        payload = data['payload']
        self.project_id = payload['projectId']
        response = self.rqst_session.post(url, data=payload,
                                          cookies={'JSESSIONID': self.jsessionid})
        read_response, self.task_id = self.verify_create(response)
        data = read_response.json()['data'][0]
        self.db_store.insert(self.scope, self.test_id, ENTITY, data)
        return self

    def read(self, **data):
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=data['entity_id'])
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    @payload_generator.generate_payload
    def update(self, **data):
        api = self.urls[ENTITY]['update']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            project_id=data['project_id'],
            entity_id=data['task_id'])
        payload = data['payload']
        response = self.rqst_session.post(url, json=payload, cookies={
            'JSESSIONID': self.jsessionid})
        self.task_id = data['task_id']
        self.verify_update(data['task_id'], response)
        payload['data'].pop('id')
        self.db_store.update_by_key(ENTITY, 'id', data['task_id'], payload['data'])

    @payload_generator.generate_payload
    def delete(self, **data):
        api = self.urls[ENTITY]['delete']
        entity_id = data['entity_id']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'])
        self.rqst_session.delete(url, json=data['payload'],
                                 cookies={'JSESSIONID': self.jsessionid})

        self.db_store.delete(ENTITY, 'id', entity_id)

    def verify_create(self, response):
        self.status = True
        self.step_desc = 'Innotas  Task create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        read_response = ''
        entity_id = ''

        if response.status_code == 200:
            entity_id = response.json()['newTaskId']
            read_response = self.read(entity_id=entity_id)
            if read_response.status_code == 200:
                self.remarks += 'Task is created'
            else:
                self.status = False
                self.remarks += 'task creation failed \n failure traceback : {}'.format(
                    response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return read_response, entity_id

    def verify_update(self, entity_id, response):
        self.status = True
        self.step_desc = 'Task update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        if response.status_code == 200:
            self.remarks += 'Task updated successfully'
        else:
            self.status = False
            self.remarks += 'Task updation failed : {}'.format(response.text)
        db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def verify_delete(self, response, artifact_id, ttl):
        pass
