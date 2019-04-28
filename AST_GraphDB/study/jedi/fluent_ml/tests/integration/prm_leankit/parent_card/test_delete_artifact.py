import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_PRM_Project'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration()


@zid('96944')
@category('work')
def test_prm_project_deletion():
    """
    Delete a synced work in PRM
    """
    PRM().Project('Auto_Project_96944', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_96944').set_lane('in_process').update()\
        .run_integration() \
        .goto_prm().Project('Auto_Project_96944').delete()\
        .run_integration() \
        .goto_lk().Card('Auto_Project_96944').verify_top_lane('in_process')\
        .goto_prm().Project('Auto_Project_96944').not_exists()


@zid('96955')
@category('work')
def test_recreate_deleted_cards_false():
    """
    Delete a synched card in Leankit when "lk_sync_recreate_deleted_cards" is false in Leankit config.ini
    """
    PRM().Project('Auto_Project_96955', lk_flag=True)\
        .run_integration() \
        .goto_lk().Card('Auto_Project_96955').delete() \
        .run_integration(integration_type='card_recreate_disabled') \
        .goto_lk().Card('Auto_Project_96955').not_exists() \
        .goto_prm().Project('Auto_Project_96955').exists()


@zid('96956')
@category('work')
def test_recreate_deleted_card_field_not_present():
    """
    Delete a synced card in Leankit when "lk_sync_recreate_deleted_cards" not added in Leankit config.ini
    """
    PRM().Project('Auto_Project_96956', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_96956').delete() \
        .run_integration(integration_type='card_recreate_enabled') \
        .goto_lk().Card('Auto_Project_96956').exists() \
                         .verify_default_top_lane() \
        .goto_prm().Project('Auto_Project_96956').exists() \
                             .verify_lk_top_lane('not_started') \
                             .verify_lk_card_lane_status('Backlog')


@zid('96942')
@category('work')
def test_delete_sync_active_card_in_lk():
    """
    PRM-LK Integ - Delete a synced card in active status in Leankit and verify its recreated after integration
    """
    PRM().Project(prm_module_project, lk_flag=True)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_lane('in_process').update()\
        .run_integration()\
        .goto_lk().Card(prm_module_project).delete()\
        .run_integration()\
        .goto_lk().Card(prm_module_project).verify_default_top_lane()\
        .goto_prm().Project(prm_module_project).verify_default_lk_top_lane()\
                             .verify_default_lk_card_lane_status()


@zid('96943')
@category('work')
def test_delete_sync_archive_card_in_lk():
    """
    PRM-LK Integ - Delete a synced card in archive status in Leankit and verify its recreated after integration
    """
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_lane('completed').update()\
        .run_integration()\
        .goto_lk().Card(prm_module_project).delete()\
        .run_integration()\
        .goto_lk().Card(prm_module_project).verify_default_top_lane()\
        .goto_prm().Project(prm_module_project).verify_default_lk_top_lane()\
                             .verify_default_lk_card_lane_status()
