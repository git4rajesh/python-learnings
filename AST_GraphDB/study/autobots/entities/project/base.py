import json

from core import utils
from core.src.json_generator import PayloadGenerator
from core.db import db_wrapper
from entities.entity import Entity

ENTITY = 'project'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.project_id = None
        self.payload_generator.request = request

    @payload_generator.generate_payload
    def create(self, **data):
        """
        Project can be created with or without template
        :param test_id: test_id of the project
        :param template: Template id
        :param data: rate parameters which is used to create a payload
        """
        payload = data['payload']
        api = self.urls[ENTITY]['create']
        if data.get('template'):
            api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            category_id=self.constants['PROJECT']['CATEGORIES']['CATEGORY1']['ID'],
            template_id=data.get('template'))

        response = self.rqst_session.post(url, json=payload,
                                          cookies={'JSESSIONID': self.jsessionid})
        read_response, self.project_id = self.verify_create(response)
        self.db_store.insert(self.scope, self.test_id, ENTITY, read_response.json()['data'][0])

    def read(self, **data):
        """
        To get the details of a given project_id
        :param data: data = {entity_id:<<project_id>>}
        :return:
        """
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=data['entity_id'])
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def read_settings(self, project_id):
        """
        To get the setting details of a given project_id
        :param project_id: project id of the project to be read with setting details (in UI: 'Settings')
        :return: response of api
        """
        api = self.urls[ENTITY]['read_settings']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=project_id)
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def read_more(self, project_id):
        """
        To get the details of a given project_id
        :param project_id: project id of the project to be read with additional details (in UI: 'Executive Summary')
        :return: response of api
        """
        api = self.urls[ENTITY]['read_more']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=project_id)
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def read_title(self, title):
        """
        To get the details of a given project_title
        :param title:  Title of the project to fetch
        :return: api response
        """
        api = self.urls[ENTITY]['read_title']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_title=title)
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        entity_id = response.json()['children'][0]['id']
        data = {'entity_id': entity_id}
        read_response = self.read(**data)
        # self.data_store.add(ENTITY, response.json(), self.ttl)
        self.db_store.insert(self.scope, self.test_id, ENTITY, response.json())

        return read_response

    @payload_generator.generate_payload
    def update(self, **data):
        """
        update the parameters of the given project_id in the db and store
        :param data: data = {entity_id:<<project_id>>}
        """
        api = self.urls[ENTITY]['update']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=data['entity_id'])
        payload = data['payload']
        response = self.rqst_session.post(url, json=payload, cookies={'JSESSIONID': self.jsessionid})
        self.verify_update(response)
        # self.data_store.update(ENTITY, data['entity_id'], **payload['data'])
        payload['data'].pop('id')
        self.db_store.update_by_key(ENTITY, 'id', data['entity_id'], payload['data'])

    @payload_generator.generate_payload
    def delete(self, **data):
        """
        delete entity from the db and store
        :param data:
        :return:
        """
        api = self.urls[ENTITY]['delete']
        entity_id = data['entity_id']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            entity_id=entity_id)
        payload = data['payload']
        self.rqst_session.post(url, json=payload, cookies={'JSESSIONID': self.jsessionid})
        self.db_store.delete(ENTITY, 'id', entity_id)

    def verify_create(self, response):
        """
        Verification is done only for the response status code
        :param response: Create response which needs to be verified
        """
        self.status = True
        self.step_desc = 'Innotas  Project create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        read_response = ''

        if response.status_code == 201:
            entity_id = response.json()['id']
            read_response = self.read(artifact_id=entity_id,
                                      entity_id=entity_id)
            if read_response.status_code == 200:
                self.remarks += 'Project is created'
            else:
                self.status = False
                self.remarks += 'project creation failed \n failure traceback : {}'.format(
                    response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return read_response, entity_id

    def verify_update(self, response):
        """
        verification of the response after the update on project entity
        for the given project_id
        :param response: response after update call
        """
        self.status = True
        self.step_desc = 'Project update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        if response.status_code == 200:
            self.remarks += 'Project updated successfully'
        else:
            self.status = False
            self.remarks += 'Project updation failed : {}'.format(response.text)
        db_wrapper.log_into_steps(self.request, self)
        assert self.status

    def verify_delete(self, response, artifact_id):
        pass
