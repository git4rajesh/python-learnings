from core.src import userpool
from entities.entity import Entity
from entities.timeadmin.timeadmin import Timeadmin
from entities.timesheet import helper
from core import utils
from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.user.user import User

ENTITY = 'timesheet'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.payload_generator.request = request

    @helper.append_entries
    @payload_generator.generate_payload
    def create(self, **data):
        payload = data['payload']
        timesheet_id = data['timesheet_id']
        api = self.urls[ENTITY]['create']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            timesheet_id=timesheet_id)
        response = self.rqst_session.post(url, json=payload, cookies={
            'JSESSIONID': self.jsessionid})

        read_response = self.verify_create(response, timesheet_id)
        self._add_timesheet_to_store(read_response, data['task_id'], timesheet_id)
        return timesheet_id

    def read(self, **data):
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            timesheet_id=data['entity_id'])
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    @payload_generator.generate_payload
    def update(self, ttl, **data):
        response = self.rqst_session.put(data['url'], json=data['payload'],
                                         cookies={
                                             'JSESSIONID': self.jsessionid})
        return response

    @payload_generator.generate_payload
    def delete(self, **data):
        timesheet_row_id = data['entity_id']
        timesheet_details = self.db_store.search_by_key(ENTITY, 'id', timesheet_row_id)[0]
        timesheet_id = timesheet_details['timesheet_id']
        api = self.urls[ENTITY]['delete']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            timesheet_id=timesheet_id)
        response = self.rqst_session.delete(url, json=data['payload'], cookies={
            'JSESSIONID': self.jsessionid})
        self.db_store.delete(ENTITY, 'id', timesheet_row_id)
        return response

    def verify_create(self, response, timesheet_id):
        self.status = True
        self.step_desc = 'Timesheet create verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)
        read_response = ''

        if response.status_code == 200:
            # Read the timesheet and corresponding internal rates from timeadmin perspective
            read_response = self.read_by_timeadmin(timesheet_id)
            if read_response.status_code == 200:
                self.remarks += 'Timesheet is created'
            else:
                self.status = False
                self.remarks += 'project creation failed \n failure traceback : {}'.format(
                    response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return read_response

    def read_by_timeadmin(self, timesheet_id):
        username_holder = userpool.get_username_current_user(self.request)
        jsessionid_holder = userpool.get_usertoken_of_current_user(self.request)
        admin_jsessionid = userpool.get_admintoken(self.request)
        if jsessionid_holder != admin_jsessionid:
            user = User(self.request, 'admin').create()
            user.login()
            read_response = Timeadmin(self.request).read(entity_id=timesheet_id)
            user.logout()
        else:
            read_response = Timeadmin(self.request).read(entity_id=timesheet_id)
        self.request.config.option.username = username_holder
        self.request.config.option.jsessionid = jsessionid_holder
        return read_response

    def verify_update(self, response, dct_expected, project_id, ttl):
        pass

    def verify_delete(self, response, artifact_id, ttl):
        pass

    def _get_entries_from_response(self, read_response, task_id):
        task_activity = []
        for activity in read_response.json()[ENTITY]['activities']:
            if 'taskId' in activity.keys() and activity['taskId'] == task_id:
                task_activity.append(activity)
        return task_activity

    def _add_timesheet_to_store(self, read_response, task_id, timesheet_id):
        task_dct = self.db_store.search_by_key('task', 'id', task_id)[0]
        task_activity_lst = self._get_entries_from_response(
            read_response, task_id)
        for task_activity in task_activity_lst:
            task_activity.update(timesheet_id=timesheet_id)
            task_activity.update(logged_user=self.request.config.option.user)
            timesheet_details = self.db_store.search_by_key(ENTITY, 'id', task_activity['id'])
            if timesheet_details:
                self.db_store.update_by_key(ENTITY, 'id', task_activity['id'], task_activity)
            else:
                self.db_store.insert(self.scope, self.test_id, ENTITY,
                                     task_activity)
            # Appending timesheet_row_ids in task details in the store
            if 'timesheet_row_ids' in task_dct.keys():
                if task_activity['id'] not in task_dct['timesheet_row_ids']:
                    task_dct['timesheet_row_ids'].append(task_activity['id'])
            else:
                task_dct['timesheet_row_ids'] = [task_activity['id']]
        self.db_store.update_by_key('task', 'id', task_id, task_dct)
