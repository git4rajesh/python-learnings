import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_Blocked_Flag'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration()


@zid('97162')
@category('work')
def test_blocked_flag_on_project_sync():
    """
    Verify LK Blocked Flag field in PRM on project sync
    """
    PRM().Project('Auto_97162', lk_flag=True) \
        .run_integration() \
        .goto_prm().Project('Auto_97162').verify_lk_blocked_flag('No')


@zid('97163')
@category('work')
def test_block_synced_card_and_sync_again():
    """
    Block synced card in Leankit and sync again
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_blocked_flag(True).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_blocked_flag('Yes')


@zid('97164')
@category('work')
def test_unblock_synced_card():
    """
    Unblock blocked synced card in Leankit and sync
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_blocked_flag(True).update() \
        .run_integration() \
        .goto_lk().Card(prm_module_project).set_blocked_flag(False).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_blocked_flag('No')
