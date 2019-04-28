from automation.core.utils.asserter import Asserter
from automation.core.utils import objectpath_wrapper
from automation.core.src.test_details import TestDetails
from automation.core.src import helper as core_helper
from automation.core.src.environment import Environment
from automation.fluent_ml.src import helper
from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.fluent_ml.leankit.features.card import Card


class LKVerify:

    def __init__(self):
        super().__init__()
        self.asserter = Asserter()
        self.db_logger = DBLoggerFactory.logger
        self.id = TestDetails.test_id
        self.uuid = TestDetails.test_uuid
        self.card = Card()
        self.env = Environment()

    def card_details(self, card_id, dct_expected):
        # card_id = dct_expected['id']

        self.status = False
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_method_class_names())
        self.step_desc = 'Verifying Card Details after Integration'
        self.step_input = 'Expected values: %s' % dct_expected

        response = self.card.read(card_id)
        status_code = response.status_code
        if status_code == 200:
            dct_actual = helper.construct_actual(response.json(), dct_expected)
            self.status, remarks = self.asserter.verify(dct_actual, expected=dct_expected)
            self.remarks += remarks
        else:
            self.remarks += 'Card Read API failed with status code: {0} and response: {1}'.format(status_code,
                                                                                                  response.text)
        self.db_logger.log_into_steps(self)
        assert self.status

    def verify_prm_ext_link_in_lk(self, card_id, prm_project_key):

        self.status = False
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_method_class_names())
        self.step_desc = 'PRM External Link verification in Leankit'
        self.step_input = 'Expected values: LK Crad ID: {0}, PRM Project Key: {1}'.format(card_id, prm_project_key)

        read_resp = self.card.read(card_id)
        status_code = read_resp.status_code
        card_name = None
        if status_code == 200:
            card_name = read_resp.json()['title']

            scode = helper.get_scode(prm_project_key)
            protocol = self.env.pve.protocol
            host_name = self.env.pve.name

            actual_external_url = objectpath_wrapper.filter_dct_for_key('label', 'Enterprise One', 'url',
                                                                        read_resp.json())[0]
            expected_url = '{protocol}://{host_name}/planview/PLP/EntityLandingPage.aspx?pt=PROJECT&scode={scode}'.format(
                protocol=protocol, host_name=host_name, scode=scode)

            self.status, remarks = self.asserter.verify(actual_external_url, expected=expected_url,
                                                        condition='is_equal_to_ignoring_case')
            self.remarks += remarks
        else:
            self.remarks += 'PRM External link is not Present in Leankit after Integration'

        self.db_logger.log_into_steps(self)
        assert self.status
        return card_name
