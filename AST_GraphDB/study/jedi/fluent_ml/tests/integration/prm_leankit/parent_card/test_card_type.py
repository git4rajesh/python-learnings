import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM


@zid('98413')
@category('work')
def test_card_type_field():
    """
    Verify LK Card Type field in PRM
    """
    PRM().Project('Auto_98413', lk_flag=True)\
        .run_integration() \
        .goto_prm().Project('Auto_98413').verify_lk_card_type() \
        .goto_lk().Card('Auto_98413', board='board1').verify_card_type()


@zid('98414')
@category('work')
def test_update_card_type_in_lk():
    """
    LK Card Type: Update card Type for a synced card in Leankit and sync again
    """
    PRM().Project('Auto_98414', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_98414').set_card_type('non_default').update() \
        .run_integration() \
        .goto_prm().Project('Auto_98414').verify_lk_card_type(card_type='non_default')
