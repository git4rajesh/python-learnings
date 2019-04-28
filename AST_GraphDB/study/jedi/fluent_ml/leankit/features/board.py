import sys
import os
import requests

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.core.src.environment import Environment
from automation.core.src import helper as core_helper
from automation.core.utils import objectpath_wrapper
from automation.core.utils.asserter import Asserter


from automation.integration.src.constants_reader import ConstantsReader

READ_URL = "{protocol}://{host_name}/io/board/{board_id}"
UPDATE_LANE_URL = "{protocol}://{host_name}/io/board/{board_id}/lane/{lane_id}"


class Board:

    def __init__(self):
        self._get_env_details()
        self.db_logger = DBLoggerFactory.logger
        self.req_session = requests.session()
        self.asserter = Asserter()

    def _get_env_details(self):
        env = Environment()
        self.protocol = env.external_env.protocol
        self.host_name = env.external_env.name

        lk_json_const = ConstantsReader.lk_json_const
        self.headers = {"Authorization": lk_json_const['token']}

    def create(self, payload):
        pass

    def update(self, board_id, lane_id, payload):
        update_url = UPDATE_LANE_URL.format(protocol=self.protocol, host_name=self.host_name, board_id=board_id, lane_id=lane_id)
        response = self.req_session.patch(update_url, json=payload, headers=self.headers)

        self.verify_update(response, board_id, lane_id, paylaod)

    def read(self, board_id):
        read_url = READ_URL.format(protocol=self.protocol, host_name=self.host_name, board_id=board_id)
        resp = self.req_session.get(read_url, headers=self.headers)
        return resp

    def delete(self, artifact_id):
        pass

    def verify_update(self, response, board_id, lane_id, dct_expected):
        self.status = False
        self.step_desc = 'Leankit Board Lane Update verification'
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_input = 'Input value board_id: {0}, lane_id: {1}'.format(board_id, lane_id)

        if response.status_code == 200:
            read_resp = self.read(board_id)
            if read_resp.status_code == 200:
                dct_actual = objectpath_wrapper.get_dct_containing_condition('id', lane_id, read_resp)
                self.status, remarks = self.asserter.verify(dct_actual, expected=dct_expected)
                self.remarks += remarks
            else:
                self.remarks += "Read Response failed with status code: {0} and response: {1}".format(
                    read_resp.status_code, read_resp.text)
        else:
            self.remarks += "Board Lane update failed with status code: {0} and response: {1}".format(response.status_code, response.text)

        self.db_logger.log_into_steps(self)
        assert self.status

    def verify_delete(self, card_id):
        pass
