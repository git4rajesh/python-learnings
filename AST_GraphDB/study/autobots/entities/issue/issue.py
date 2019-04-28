from entities.issue.base import Base

ENTITY = 'issue'


class Issue(Base):

    def __init__(self, request):
        super().__init__(request)

    def create(self, title):
        """
        Atom to create the issue
        :return: self object
        """
        data = {'title': title, 'project_id': self.project_id}
        super().create(**data)
        return self

    def delete(self, entity_details=None):
        """
        Atom to delete the issues which calls base delete
        :return: self object
        """
        if not entity_details:
            entity_id = self.issue_id
        else:
            entity_id = entity_details['id']
        super().delete({'entity_id': entity_id})
        return self
