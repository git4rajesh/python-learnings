from entities.asset.base import Base

ENTITY = 'asset'


class Asset(Base):

    def __init__(self, request):
        super().__init__(request)

    def create(self, title=None):
        """
        Atom to create the asset
        :return: self object
        """
        data = {'title': title}
        super().create(**data)
        return self

    def delete(self, entity_details=None):
        """
        Atom to delete the portfolios which calls base delete
        :return: self object
        """
        if not entity_details:
            entity_id = self.asset_id
        else:
            entity_id = entity_details['id']
        super().delete({'entity_id': entity_id})
        return self
