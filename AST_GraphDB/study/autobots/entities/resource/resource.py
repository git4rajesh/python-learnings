import random

from core import utils
from entities.resource.base import Base

ENTITY = 'resource'


class Resource(Base):
    def __init__(self, request):
        super().__init__(request)

    def create(self):
        """
        Atom to create a resource
        :return:
        """
        name = utils.get_title(ENTITY)
        data = {'firstname': name}
        super().create(**data)
        return self
