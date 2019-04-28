import sys
import os
import requests

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.datastore.tinydb_datastore import DataStore
from automation.core.src.test_details import TestDetails
from automation.core.src.environment import Environment
from automation.core.src import helper as core_helper
from automation.core.utils.asserter import Asserter
from automation.core.utils import objectpath_wrapper

from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.integration.src.constants_reader import ConstantsReader
from automation.fluent_ml.src import helper

CREATE_URL = "{protocol}://{host_name}/io/card"
UPDATE_READ_DEL_URL = "{protocol}://{host_name}/io/card/{card_id}"
MOVE_URL = "{protocol}://{host_name}/io/card/move"


class Card:
    tbl_name = 'LK_Card'

    def __init__(self):
        self._get_env_details()
        self.req_session = requests.session()
        self.db_logger = DBLoggerFactory.logger
        self.asserter = Asserter()

        self.id = TestDetails.test_id
        self.uuid = TestDetails.test_uuid
        self.scope = TestDetails.scope

    def _get_env_details(self):
        env = Environment()
        self.protocol = env.external_env.protocol
        self.host_name = env.external_env.name

        lk_json_const = ConstantsReader.lk_json_const
        self.headers = {"Authorization": lk_json_const['token']}

    def create(self, payload):
        create_url = CREATE_URL.format(protocol=self.protocol, host_name=self.host_name)
        response = self.req_session.post(url=create_url, json=payload, headers=self.headers)
        card_id = self.verify_create_update(response, payload)

        DataStore.insert(Card.tbl_name, id=card_id, name=payload['title'], scope=self.scope, test_id=self.id, **payload)
        print("*****LK_CARD TABLE*****\n", DataStore.read_all('LK_Card'))
        return card_id

    def update(self, card_id, payload):
        update_url = UPDATE_READ_DEL_URL.format(protocol=self.protocol, host_name=self.host_name, card_id=card_id)
        response = self.req_session.patch(update_url, json=payload, headers=self.headers)

        expected_dct = {}
        for dct in payload:
            expected_key = dct['path'].split('/')[-1]
            expected_value = dct['value']
            expected_dct[expected_key] = expected_value

        self.verify_create_update(response, expected_dct)

        if 'title' in expected_dct:
            dct_update_ds = {'name': expected_dct['title']}
            DataStore.update(Card.tbl_name, dct_update_ds, id=card_id)
        else:
            DataStore.update(Card.tbl_name, expected_dct, id=card_id)

        print("*****LK_CARD TABLE*****\n", DataStore.read_all('LK_Card'))

    def move(self, card_id, payload):
        url = MOVE_URL.format(protocol=self.protocol, host_name=self.host_name)
        response = self.req_session.post(url, json=payload, headers=self.headers)

        dct_expected = payload['destination']

        self.verify_move(card_id, response, dct_expected)
        DataStore.update(Card.tbl_name, dct_expected, id=card_id)
        print("*****LK_CARD TABLE*****\n", DataStore.read_all('LK_Card'))

    def read(self, artifact_id):
        read_url = UPDATE_READ_DEL_URL.format(protocol=self.protocol, host_name=self.host_name, card_id=artifact_id)
        response = self.req_session.get(read_url, headers=self.headers)
        return response

    def delete(self, artifact_id):
        delete_url = UPDATE_READ_DEL_URL.format(protocol=self.protocol, host_name=self.host_name, card_id=artifact_id)
        self.req_session.delete(delete_url, headers=self.headers)
        self.verify_delete(artifact_id)
        DataStore.delete(Card.tbl_name, id=artifact_id)
        # On explicit deletion of a card, corresponding external_id column should be removed in PRM_Project Table
        DataStore.delete_column('PRM_Project', 'external_id', external_id=artifact_id)
        print("*****LK_CARD TABLE*****\n", DataStore.read_all('LK_Card'))
        print("*****PRM_PROJECT TABLE AFTER EXTERNAL_ID POP UP*****\n", DataStore.read_all('PRM_Project'))

    def verify_create_update(self, response, dct_expected):
        self.status = False
        self.step_desc = 'Leankit Card create/update verification'
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_input = 'Expected response is {}'.format(dct_expected)

        card_id = None

        if response.status_code in (200, 201):
            card_id = response.json().get('id')
            read_resp = self.read(card_id)
            if read_resp.status_code == 200:
                dct_expected, dct_actual = self.construct_expected_actual_dct(dct_expected, read_resp)
                self.status, remarks = self.asserter.verify(dct_actual, expected=dct_expected)
                self.remarks += remarks
            else:
                self.remarks += "Read Response failed with status code: {0} and response: {1}".format(
                    read_resp.status_code, read_resp.text)
        else:
            self.remarks += "Card Creation/update failed with status code: {0} and response: {1}".format(
                response.status_code,
                response.text)

        self.db_logger.log_into_steps(self)
        assert self.status, self.remarks
        return card_id

    def verify_move(self, card_id, response, dct_expected):
        self.status = False
        self.step_desc = 'Leankit Card Move verification'
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_input = 'Input value card_id: {0}'.format(card_id)

        if response.status_code == 200:
            read_resp = self.read(card_id)
            if read_resp.status_code == 200:
                dct_expected, dct_actual = self.construct_expected_actual_dct(dct_expected, read_resp)
                self.status, remarks = self.asserter.verify(dct_actual, expected=dct_expected)
                self.remarks += remarks
            else:
                self.remarks += "Read Response failed with status code: {0} and response: {1}".format(
                    read_resp.status_code, read_resp.text)
        else:
            self.remarks += "Card Move failed with status code: {0} and response: {1}".format(
                response.status_code,
                response.text)

        self.db_logger.log_into_steps(self)
        assert self.status, self.remarks
        return card_id

    def verify_delete(self, card_id):
        self.status = False
        self.step_desc = 'Leankit Card delete verification'
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_input = 'Input value {}'.format(card_id)

        read_resp = self.read(card_id)

        if read_resp.status_code == 404:
            expected_msg = 'Not found.'
            actual_msg = read_resp.json()['message']

            self.status, remarks = self.asserter.verify(actual_msg, expected=expected_msg,
                                                        condition='is_equal_to')
            self.remarks += remarks
        else:
            self.remarks += 'Card is not deleted'

        self.db_logger.log_into_steps(self)
        assert self.status, self.remarks

    def construct_expected_actual_dct(self, dct_expected, read_resp):
        if 'connections' in dct_expected:
            exp_parent_card_id = dct_expected['connections']['parents'][0]
            dct_expected.pop('connections')

            actual_parent_card_id = objectpath_wrapper.filter_dct_for_key('cardId', exp_parent_card_id, 'cardId',
                                                                          read_resp.json())[0]
            dct_actual = helper.construct_actual(read_resp.json(), dct_expected)

            dct_expected.update({'parent_card_id': exp_parent_card_id})
            dct_actual.update({'parent_card_id': actual_parent_card_id})
        else:
            dct_actual = helper.construct_actual(read_resp.json(), dct_expected)

        return dct_expected, dct_actual
