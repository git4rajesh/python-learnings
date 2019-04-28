from abc import abstractmethod

import requests

from core.src import userpool


class Rollup():

    def __init__(self, request):
        self.rqst_session = requests.session()
        self.request = request
        self.jsessionid = userpool.get_usertoken_of_current_user(self.request)
        self.urls = request.getfixturevalue('read_urls')
        self.db_store = request.getfixturevalue('tiny_db_store')
        self.cmd_options = request.getfixturevalue('set_cmdline_opts')

    @abstractmethod
    def verify_rollups(self):
        pass
