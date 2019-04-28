from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.entity import Entity
from core import utils

ENTITY = 'resource'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.payload_generator.request = request

    @payload_generator.generate_payload
    def create(self, **data):
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'])
        response = self.rqst_session.post(url, data=data['payload'],
                                          cookies={'JSESSIONID': self.jsessionid},
                                          headers={
                                              'Content-Type': 'application/x-www-form-urlencoded'}
                                          )

        read_response, self.resource_id = self.verify_create(response, **data)
        data = read_response.json()['data'][0]
        self.db_store.insert(self.scope, self.test_id, ENTITY, data)
        return self

    def read(self, firstname, lastname):
        api = self.urls[ENTITY]['read']
        url = api.format(protocol=self.constants['SERVER']['PROTOCOL'], env=self.cmd_options['env'],
                         firstname=firstname,
                         lastname=lastname)
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        return response

    def update(self):
        pass

    def delete(self, data):
        pass

    def verify_create(self, response, **data):
        self.status = True
        self.step_desc = 'Innotas Resource create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = response.text
        read_response = ''

        if response.status_code == 200:
            read_response = self.read(data['firstname'], 'auto_bots')
            expected_title = ", ".join(['auto_bots', data['firstname']])
            if read_response.status_code == 200:
                data = read_response.json()['data']
                is_resource_created = False
                for resource in data:
                    if expected_title.lower() == resource['t_title'].lower():
                        id = resource['id']
                        self.remarks += 'Resource is created'
                        is_resource_created = True
                if not is_resource_created:
                    self.status = False
                    self.remarks += 'resource creation failed \n failure traceback : {}'.format(response.text)
            else:
                self.status = False
                self.remarks += 'resource creation failed \n failure traceback : {}'.format(response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return read_response, id

    def verify_update(self, *args, **kwargs):
        pass

    def verify_delete(self, *args, **kwargs):
        pass
