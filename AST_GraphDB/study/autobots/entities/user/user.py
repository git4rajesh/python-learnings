import random

from core import utils
from core.src import userpool
from entities.resource.resource import Resource
from entities.user.base import Base
from entities.user.rate.rate import Rate

ENTITY = 'user'


class User(Base):
    def __init__(self, request, username=None, usertype='Full'):
        super().__init__(request)
        self.username = username.lower() if username else 'admin'
        self.usertype = usertype
        if self.username == 'admin':
            if not userpool.is_username_in_pool(self.request, self.username):
                userid = self.request.config.option.constants['USERS']['ADMIN']['USERID']
                resourceid = self.request.config.option.constants['USERS']['ADMIN']['RESOURCEID']
                userpool.update_user_pool(self.request, self.username, userid, resourceid)

    def create(self):
        if userpool.is_username_in_pool(self.request, self.username):
            return self
        resource = Resource(self.request).create()
        userid = utils.get_title(self.username)
        # TODO: put in constants file and  Full user confirm usertype required
        usertype_dct = {'support': 5, 'team': 4, 't&e': 3}
        usertype_id = usertype_dct.get(self.usertype.lower())
        if self.usertype.lower() == 'full':
            data = {'payload': 'default'}
        else:
            data = {'payload': 'specified_user_type'}
        data.update({'resource_id': resource.resource_id, 'user_type': usertype_id, 'user_id': userid,
                     'password': 'innotas', })
        super().create(**data)
        userpool.update_user_pool(self.request, self.username, userid, resource.resource_id)
        return self

    def login(self):
        userid = userpool.get_userid_from_pool(self.request, self.username)
        pwd = 'innotas'
        jsessionid = super().login_user(userid, pwd)
        userpool.update_current_user(self.request, self.username, jsessionid)
        from core.fluent import Fluent
        fluent = Fluent(self.request)
        return fluent

    def delete(self, entity_details):
        super().delete(entity_id=entity_details['user_id'])

    def logout(self):
        super().logout_user()
        user_obj = User(self.request, 'admin').login()
        return user_obj

    def set_internalrate(self, rate, days_offset=1):
        """
        set internal rate for the user
        :param rate:
        :param days_offset:
        :return:
        """
        self.rate = Rate(self.request)
        resource_id = userpool.get_resourceid_from_pool(self.request, self.username)
        self.rate.set_rate(rate, resource_id, days_offset)
        return self
