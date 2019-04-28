import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM


@zid('97151')
@category('work')
def test_default_priority():
    """
    Default Priority of Leankit Card should be synced on project sync
    """
    PRM().Project('Auto_97151', lk_flag=True) \
        .run_integration() \
        .goto_prm().Project('Auto_97151').verify_lk_priority( 'Normal')


@zid('97152')
@category('work')
def test_update_priority():
    """
    Update the Priority of synced card in Leankit and sync again
    """
    PRM().MultipleProjects(['Auto_97152_1', 'Auto_97152_2', 'Auto_97152_3'], lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_97152_1').set_priority('high').update() \
                  .goto_card('Auto_97152_2').set_priority('critical').update() \
                  .goto_card('Auto_97152_3').set_priority('low').update() \
        .run_integration() \
        .goto_prm().Project('Auto_97152_1').verify_lk_priority('High') \
                   .goto_project('Auto_97152_2').verify_lk_priority('Critical') \
                   .goto_project('Auto_97152_3').verify_lk_priority('Low')
