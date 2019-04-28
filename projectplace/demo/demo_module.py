import requests
from requests_oauthlib import OAuth1
from datetime import datetime


PP_URL_old = 'https://integration-in.rnd.projectplace.com/api/v'
PP_URL = 'https://rnd3.demo.projectplace.com/api/v'
HEADERS = {'content-type': 'application/json'}


class Demo_Module:

    def get_oauth(self):
        CLIENT_KEY = '2fbf522ed6ba4f07723f9347d6aaf2c3'
        CLIENT_SECRET = '6d6d7d95edacc1e7a337ae26792c41d9844054ba'
        access_token_key = 'bd30188e8959094ada5e184fcf850d6b'
        access_token_secret = '02cacf3cb22666759df7484323f671c666972b63'
        oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=access_token_key,
                       resource_owner_secret=access_token_secret)
        return oauth


    def list_projects(self):
        complete_url = PP_URL + self.get_version() + '/account/projects'
        resp = requests.get(url=complete_url, auth = self.get_oauth())
        proj_list = resp.json()["projects"]

        print(proj_list)

        list_prj_ids = []
        for project in proj_list:
            list_prj_ids.append(project['id'])
        print(list_prj_ids)
        return list_prj_ids

    def get_version(self):
        return str(1)

    def call_delete_project(self):
        for project_id in self.list_projects():
            self.delete_project(project_id)

    def delete_project(self, project_id):
        complete_url = PP_URL + self.get_version() + '/projects/' + str(project_id)
        requests.delete(url=complete_url, auth=self.get_oauth())

    def generate_name(self, project_name):
        timestamp = str(datetime.now()).replace(' ', '_').replace('.', '_')
        description = 'Auto_%(name)s_%(timestamp)s' % {'name': project_name,
                                                       'timestamp': timestamp}
        return description

    def create_project(self, project_name, owner_email='rvenkataraman@planview.com'):
        workspace_name = self.generate_name(project_name)
        payload = {"name": workspace_name
                   }
        complete_url = PP_URL + self.get_version() + '/account/projects/'
        response = requests.post(url=complete_url, json=payload, auth=self.get_oauth())
        return response.json()['id']

    def set_sync_flag(self, project_id):
        complete_url = PP_URL + self.get_version() + '/account/projects/' + str(project_id) + '/planview-connection'
        payload = { "external_id": "9" }
        response = requests.post(url=complete_url, json=payload, auth=self.get_oauth())
        print(response.content)

    def update_project(self, project_id):
        complete_url = PP_URL + self.get_version() + '/projects/' + str(project_id) + '/'
        print(complete_url)
        payload = {
            "archived":"false",
            "cost_code": "100",
            "custom_field":"My Custom Field",
            "description": "Updated Desc",
            "name":"Updated Name"
        }
        response = requests.post(url=complete_url, json=payload, auth=self.get_oauth())
        print(response)


    def read_projects(self, project_id):
        complete_url = PP_URL + self.get_version() + '/projects/' + str(project_id) + '/'
        response = requests.get(url=complete_url, auth=self.get_oauth())
        print(response.content)


if __name__ == '__main__':
    demo_obj = Demo_Module()

    project_id = demo_obj.create_project('MyProject')
    demo_obj.set_sync_flag(project_id)
    demo_obj.update_project(project_id)
    demo_obj.read_projects(project_id)
    # demo_obj.list_projects()
    #
    # demo_obj.call_delete_project()

