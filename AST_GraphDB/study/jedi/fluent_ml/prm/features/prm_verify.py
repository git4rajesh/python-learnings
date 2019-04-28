from automation.core.utils.asserter import Asserter
from automation.core.src import helper as core_helper
from automation.core.src.test_details import TestDetails
from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.fluent_ml.prm.db.query_handler import QueryHandler
from automation.fluent_ml.src import helper


class PRMVerify:

    def __init__(self):
        super().__init__()
        self.asserter = Asserter()
        self.db_logger = DBLoggerFactory.logger
        self.id = TestDetails.test_id
        self.uuid = TestDetails.test_uuid
        self.qhandler = QueryHandler()

    def project_details(self, project_id, dct_expected):
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_desc = 'Verifying Project Details after Integration'
        self.step_input = 'Expected values: %s' % dct_expected

        dct_actual = self.qhandler.select_project_details(project_id)

        self.status, remarks = self.asserter.verify(dct_actual, expected=dct_expected)
        self.remarks += remarks

        self.db_logger.log_into_steps(self)
        assert self.status

    def verify_lk_ext_id_in_prm(self, project_key):
        scode = helper.get_scode(project_key)
        external_id = self.qhandler.select_external_id(scode)

        self.status = False
        self.step_input = str(external_id)
        self.step_desc = 'Leankit External ID verification in PRM'
        self.remarks = '\n Inside class: %s method: %s \n' % core_helper.get_method_class_names()

        if external_id:
            self.status = True
            self.remarks += 'Leankit External Id is present in PRM'
        else:
            self.remarks += 'Leankit External Id is not present in PRM'

        self.db_logger.log_into_steps(self)
        assert self.status
        return external_id

    def project_description(self, project_id, expected_description):
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_desc = 'Verifying Project Description after Integration'
        self.step_input = 'Expected Description: %s' % expected_description
        actual_description = ''

        description = self.qhandler.select_project_description(project_id)
        # Logic to concatenate the work description as they are stored in multiple rows when they are more than 1000 characters
        if description:
            desc_generator = (''.join(row[0]) for row in description)
            actual_description = ''.join(desc_generator)

        self.status, remarks = self.asserter.verify(actual_description, expected=expected_description,
                                                    condition='is_equal_to_ignoring_case')
        self.remarks += remarks

        self.db_logger.log_into_steps(self)
        assert self.status

    def project_name(self, project_id, expected_name):
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())
        self.step_desc = 'Verifying Project Name after Integration'
        self.step_input = 'Expected Name: %s' % expected_name

        if project_id:
            actual_name = self.qhandler.select_project_name(project_id)

            self.status, remarks = self.asserter.verify(actual_name, expected=expected_name,
                                                        condition='is_equal_to_ignoring_case')
            self.remarks += remarks
        else:
            self.status = False
            self.remarks += 'Invalid Project Id : {}'.format(project_id)

        self.db_logger.log_into_steps(self)
        assert self.status
