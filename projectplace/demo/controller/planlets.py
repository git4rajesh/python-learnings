import requests
from src.oauth_gen import Oauth_Gen

from controller.decorators.planlets import Decorators_Planlets


class Planlets:
    decorator = Decorators_Planlets()

    def __init__(self):
        self.oauth_gen = Oauth_Gen()

    @decorator.construct_payload
    @decorator.construct_url
    def create(self, *args, **payload):
        response = requests.post(url=Planlets.decorator.complete_url, json=Planlets.decorator.payload,
                                 auth=self.oauth_gen.get_oauth())
        self.planlet_id = response.json()['data'][0]['id']
        self.workspace_id = payload['payload_key']['project_id']
        self.expected_planlet_name = payload['payload_key']['name']

        status = self.verify_create()
        return response.json()['data'][0]['id'], status

    @decorator.construct_payload
    @decorator.construct_url
    def edit(self, *args, **payload):
        self.expected = payload['payload_key']
        response = requests.post(url=Planlets.decorator.complete_url, json=Planlets.decorator.payload,
                                 auth=self.oauth_gen.get_oauth())
        status = self.verify_edit()
        return response.json()['data'][0]['id'], status

    @decorator.read_url
    def read(self, *args, **data):
        response = requests.get(url=Planlets.decorator.complete_read_url, auth=self.oauth_gen.get_oauth())
        return response

    @decorator.construct_payload
    @decorator.construct_url
    def delete(self, *args, **payload):
        requests.post(url=Planlets.decorator.complete_url, json=Planlets.decorator.payload,
                                 auth=self.oauth_gen.get_oauth())
        status = self.verify_delete()
        return status

    def verify_create(self):
        status = False
        response = self.read(planlet_id=self.planlet_id, project_id=self.workspace_id)
        actual_planlet_name = response.json()['name']
        if self.expected_planlet_name == actual_planlet_name:
            status = True
        return status

    def verify_edit(self):
        lst_status = []
        status = False
        actual = {}
        response = self.read(planlet_id=self.planlet_id, project_id=self.workspace_id)
        for key in self.expected:
            actual[key] = response.json()[key]

        print('Actual', actual)
        print('Expected', self.expected)
        if all(lst_status):
            status = True
        return status

    def verify_delete(self):
        status = False
        response = self.read(planlet_id=self.planlet_id, project_id=self.workspace_id)
        if response.json()['error_code'] == 'SERVER_ERROR':
            status = True

        return status

