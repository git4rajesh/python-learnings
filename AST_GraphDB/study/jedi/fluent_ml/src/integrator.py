from automation.core.logger import handler as logger
from automation.core.src.test_details import TestDetails
from automation.core.datastore.tinydb_datastore import DataStore
from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.integration.src.start_integration import IntegrationServer
from automation.fluent_ml.prm.features.project import Project
from automation.fluent_ml.prm.features.prm_verify import PRMVerify
from automation.fluent_ml.leankit.features.lk_verify import LKVerify
from automation.fluent_ml.leankit.features.card import Card


def start_integration(integration_type):
    logger.logs("Running PRM Leankit Integration", 'info')
    db_logger = DBLoggerFactory.logger
    id = TestDetails.test_id
    uuid = TestDetails.test_uuid
    integration = IntegrationServer()
    integ_status = integration.start(id, uuid, db_logger, integration_type)
    assert integ_status


def update_lk_details_in_ds():
    lst_prj_details = DataStore.read_all('PRM_Project')

    for prj_details in lst_prj_details:
        if 'external_id' not in prj_details:
            project_key = prj_details.get('id')
            prm_verify_obj = PRMVerify()
            external_id = prm_verify_obj.verify_lk_ext_id_in_prm(project_key)
            update_external_id(Project.tbl_name, external_id, project_key)
            update_card_details_in_ds(external_id, project_key)

    print("*****update_lk_details_in_ds*****\n", DataStore.read_all('PRM_Project'))


def update_external_id(table, external_id, project_key):
    dct_update = {'external_id': external_id}
    DataStore.update(table, dct_update, id=project_key)


def update_card_details_in_ds(card_id, project_key):
    card = Card()
    tbl_name = card.tbl_name

    lk_verify_obj = LKVerify()
    card_name = lk_verify_obj.verify_prm_ext_link_in_lk(card_id, project_key)

    card_details = {'id': card_id, 'name': card_name, 'external_id': project_key, 'scope': TestDetails.scope,
                    'test_id': TestDetails.test_id}
    DataStore.insert(tbl_name, **card_details)
    print("*****update_card_details_in_ds*****\n", DataStore.read_all('LK_Card'))
