import requests

from core import utils
from core.db import db_wrapper
from core.src import userpool
from core.src.json_generator import PayloadGenerator
from entities.user.rate.rate import Rate

ENTITY = 'user'


class Base():
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        self.request = request
        self.scope = request.scope
        self.test_id = request.config.option.test_id
        self.payload_generator.request = request
        self.rqst_session = requests.session()
        self.urls = request.getfixturevalue('read_urls')
        self.cmd_options = request.getfixturevalue('set_cmdline_opts')
        self.constants = request.config.option.constants
        self.db_store = request.getfixturevalue('tiny_db_store')

    @payload_generator.generate_payload
    def create(self, **data):
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'])

        from entities.user.user import User
        response = self.rqst_session.post(url, json=data['payload'],
                                          cookies={  # TODO:Remove admin
                                              'JSESSIONID': userpool.get_usertoken_of_current_user(self.request)},
                                          )
        self.verify_create(response)
        self.db_store.insert(self.scope, self.test_id, ENTITY, data)

    def read(self):
        pass

    def update(self, ttl, **data):
        pass

    def delete(self, **data):
        # get the user rate table
        user_id = data.get('entity_id')
        user_details = self.db_store.search_by_key('user', 'user_id', user_id)[0]
        rate_lst = user_details['rates']
        if rate_lst:
            for rate in rate_lst:
                rate.update(resource_id=user_id)
                Rate(self.request).delete(**rate)

    def login_user(self, user_id, pwd):
        api = self.urls[ENTITY]['login']
        url = api.format(protocol=self.constants['SERVER']['PROTOCOL'],
                         env=self.cmd_options['env'])
        response = self.rqst_session.post(url=url, data={'login': user_id, 'password': pwd})
        jsessionid = self.get_api_jsessionid(response)
        return jsessionid

    def logout_user(self):
        # logs out the user
        api = self.urls[ENTITY]['logout']
        url = api.format(protocol=self.constants['SERVER']['PROTOCOL'],
                         env=self.cmd_options['env'])
        from entities.user.user import User
        # TODO:Remove admin
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': userpool.get_usertoken_of_current_user(self.request)})

    def _make_api_request(self):
        try:
            response = self.rqst_session.post(url=self.url, \
                                              data={'login': self.user_name, 'password': self.pwd}, \
                                              headers={'Content-Type': 'application/x-www-form-urlencoded'}, )
        except (TimeoutError, self.rqst_session.exceptions.ConnectionError):
            raise self.rqst_session.exceptions.ConnectionError
        return response

    def get_api_jsessionid(self, response):
        if response.status_code == 200:
            jsessionid = self.rqst_session.cookies['JSESSIONID']
            return jsessionid

    def verify_create(self, response):
        self.status = True
        self.step_desc = 'Innotas  Resource create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)

        if response.status_code == 201:
            self.remarks += 'User is created'
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return response

    def verify_update(self, *args, **kwargs):
        pass

    def verify_delete(self, *args, **kwargs):
        pass
