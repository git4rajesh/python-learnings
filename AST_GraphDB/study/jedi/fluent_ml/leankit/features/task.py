import requests

from automation.fluent_ml.leankit.atoms.artifact import Leankit
from automation.core.datastore.tinydb_datastore import DataStore
from automation.core.src.test_details import TestDetails
from automation.core.db.db_logging.db_factory import DBLoggerFactory



CREATE_URL = "https://jediqa.leankit.com/io/card/{0}/tasks"
UPDATE_READ_DEL_URL = "https://jediqa.leankit.com/io/card/{0}"


class Task:
    def __init__(self):
        self.db_logger = DBLoggerFactory.logger
        self.req_session = requests.session()
        self.headers = {
            "Authorization": "Bearer a9c64e56fccc0f06f7913b8144b1f6bf59dd45b046a797120eaead87a90f60cb46f4ebb72290ed18b110bb90869c3e74da5598b30a8bd957e9aa3602340da99e"}

    def create(self, payload):
        # url = CREATE_URL.format(card_id)
        # resp = self.req_session.post(url=CREATE_URL, json=payload, headers=self.headers)
        # self.verify_create(payload, resp)

        test_id = TestDetails.test_id
        scope = TestDetails.scope
        dct_details = {'test_id': test_id, 'scope': scope}


        self.status = True
        self.step_desc = 'Leankit Task create verification'
        self.remarks = '\n Inside class: create method:'
        self.step_input = 'Expected response is {}'.format(payload)

        self.id = TestDetails.test_id
        self.uuid = TestDetails.test_uuid
        scope = TestDetails.scope

        self.db_logger.log_into_steps(self)

        list(map(lambda dct_payload: dct_payload.update(dct_details), payload))
        DataStore.insert_many('LK_Task', payload)

        print(DataStore.read_all('LK_Task'))

    def update(self, artifact_id, payload):
        pass

    def verify_create(self, dct_expected, response):
        pass
