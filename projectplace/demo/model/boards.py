import requests
from src.oauth_gen import Oauth_Gen
from model.artifact import Artifacts




class Boards(Artifacts):
    def __init__(self):
        self.oauth_gen = Oauth_Gen()

    def get_version(self):
        return str(1)

    def create(self, workspace_id, payload):
        complete_url = Artifacts.base_url + self.get_version() + '/projects/' + str(workspace_id) + '/boards/create-new'
        response = requests.post(url=complete_url, json=payload, auth=self.oauth_gen.get_oauth())
        return response

    def read(self, board_id):
        complete_url = Artifacts.base_url + self.get_version() + '/boards/' + str(board_id)
        response = requests.get(url=complete_url, auth=self.oauth_gen.get_oauth())
        return response
