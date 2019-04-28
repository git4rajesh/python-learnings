from core import utils
from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.entity import Entity

ENTITY = 'asset'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.asset_id = None
        self.payload_generator.request = request

    @payload_generator.generate_payload
    def create(self, **data):
        """
        Asset can be created via api
        :param test_id: test_id of the project
        :param template: Template id
        :param data: rate parameters which is used to create a payload
        """
        payload = data['payload']
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            category_id=self.constants['ASSET']['CATEGORIES']['CATEGORY1']['ID'])

        response = self.rqst_session.post(url, json=payload,
                                          cookies={'JSESSIONID': self.jsessionid})
        read_response, self.project_id = self.verify_create(response)
        self.db_store.insert(self.scope, self.test_id, ENTITY, read_response.json()['data'][0])

    def read(self, data):
        """
        To get the details of a given asset_id
        :param data: data = {entity_id:<<issue_id>>}
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

    def read_category(self):
        """
        To get all details of the asset categories
        :return: api response
        """
        api = self.urls[ENTITY]['read_category']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'])
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def read_title(self, title, class_id):
        """
        To get the details of a given asset_title
        :param title:  Title of the asset to fetch
        :return: api response
        """
        api = self.urls[ENTITY]['read_title']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            title=title,
            class_id=class_id)
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        entity_id = response.json()['data'][0]['id']
        data = {'entity_id': entity_id}
        read_response = self.read(data)
        self.db_store.insert(self.scope, self.test_id, ENTITY, response.json())
        return read_response

    def update(self):
        pass

    def delete(self, data):
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
        payload = {'id': data['entity_id']}
        self.rqst_session.post(url, json=payload,
                               cookies={'JSESSIONID': self.jsessionid})
        self.db_store.delete(ENTITY, 'id', entity_id)

    def verify_update(self, *args, **kwargs):
        pass

    def verify_delete(self, *args, **kwargs):
        pass

    def verify_create(self, response):
        """
        Verification is done only for the response status code
        :param response: Create response which needs to be verified
        """
        self.status = True
        self.step_desc = 'Innotas Asset create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        read_response = ''

        if response.status_code == 201:
            entity_id = response.json()['id']
            read_response = self.read({'entity_id': entity_id})
            if read_response.status_code == 200:
                self.remarks += 'Asset is created'
            else:
                self.status = False
                self.remarks += 'asset creation failed \n failure traceback : {}'.format(
                    response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return read_response, entity_id