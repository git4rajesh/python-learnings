import requests
from abc import ABCMeta, abstractmethod

from core.src import userpool


class Entity(metaclass=ABCMeta):
    def __init__(self, request):
        self.rqst_session = requests.session()
        self.request = request
        self.jsessionid = userpool.get_usertoken_of_current_user(self.request)
        self.urls = request.getfixturevalue('read_urls')
        # self.data_store = request.getfixturevalue('data_store')
        self.db_store = request.getfixturevalue('tiny_db_store')
        self.cmd_options = request.getfixturevalue('set_cmdline_opts')
        self.constants = request.config.option.constants
        self.test_id = request.config.option.test_id
        self.scope = request.scope

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    def verify_create(self, *args, **kwargs):
        pass

    @abstractmethod
    def verify_update(self, *args, **kwargs):
        pass

    @abstractmethod
    def verify_delete(self, *args, **kwargs):
        pass
