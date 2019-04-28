from entities.rollups.rollupfactory import RollupFactory
from entities.timesheet.base import Base
from entities.timesheet.log import Log
from entities.user.user import User

ENTITY = 'timesheet'


class Timesheet(Base):

    def __init__(self, request):
        super().__init__(request)
        self.timesheet_id = None
        self.task_id = None

    def log(self, title):
        log = Log(self).select_a_task(title)
        return log

    def submit(self, **data):
        api = self.urls[ENTITY]['update']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
        )
        url = '{url}/{timesheet_id}?submit=true'.format(url=url, timesheet_id=self.timesheet_id)
        data.update(url=url, payload='submit')
        super().update(**data)
        return self

    def approve(self, **data):
        api = self.urls[ENTITY]['update']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
        )
        url = url + '?approver=true'
        data.update(url=url, payload='approve', timesheet_id=self.timesheet_id)
        super().update(**data)
        return self

    def logout(self):
        User(self.request, self.request.config.option.username).logout()
        return self

    def delete(self, entity_details):
        super().delete(entity_id=entity_details['id'])

    def verify_rollups(self, entity_type):
        """
        Atom to call the RollupFactory, and calls the entity rollup verification internally
        :param entity_type: entity type for which rollup is needed
        :return: self object
        """
        entity = RollupFactory.get_rollup_entity(self.request, entity_type, self.task_id, self.project_id)
        entity.verify_rollups()
