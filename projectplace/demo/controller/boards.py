import requests
from src.oauth_gen import Oauth_Gen

from controller.decorators.boards import Decorators_Board

class Boards:
    base_url = 'https://rnd3.demo.projectplace.com/api/v1'

    decorator = Decorators_Board()

    def __init__(self, workspace_id, board_name):
        self.workspace_id = workspace_id
        self.board_name = board_name
        self.oauth_gen = Oauth_Gen()


    @decorator.create_url
    @decorator.create_payload
    def create(self, workspace_id):
        response = requests.post(url=Boards.decorator.complete_create_url, json=Boards.decorator.payload,
                                 auth=self.oauth_gen.get_oauth())
        self.board_id = response.json()['id']

        status = self.verify_create()
        return response.json()['id'], status

    @decorator.read_delete_update_url
    def read(self, board_id):
        response = requests.get(url=Boards.decorator.complete_url, auth=self.oauth_gen.get_oauth())
        return response

    @decorator.read_delete_update_url
    # @decorator.update_payload
    def update(self, board_id, payload ):
        self.expected = payload
        response = requests.post(url=Boards.decorator.complete_url, json=payload,
                                 auth=self.oauth_gen.get_oauth())
        if self.expected['is_archived'] == 'true':
            self.expected['is_archived'] = True
        else:
            self.expected['is_archived'] = False

        status = self.verify_update()
        return response, status

    @decorator.read_delete_update_url
    def delete(self, board_id):
        response = requests.delete(url=Boards.decorator.complete_url, auth=self.oauth_gen.get_oauth())
        status = self.verify_delete()
        return response, status


    def verify_create(self):
        status = False
        response = self.read(self.board_id)
        expected_board_name = Boards.decorator.board_name
        actual_board_name = response.json()['name']

        if expected_board_name == actual_board_name:
            status = True

        return status

    def verify_update(self):
        lst_status = []
        status = False
        actual = {}
        response = self.read(self.board_id)
        for key in self.expected:
            actual[key] = response.json()[key]

        for key in self.expected:
            if actual[key] == self.expected[key]:
                lst_status.append(True)
            else:
                lst_status.append(False)

        print('Actual', actual)
        print('Expected', self.expected)
        if all(lst_status):
            status = True
        return status

    def verify_delete(self):
        status = False
        response = self.read(self.board_id)
        if response.json()['error_code'] == 'NOT_FOUND_BOARD':
            status = True

        return status





