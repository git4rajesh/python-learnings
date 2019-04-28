import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM


@zid('96953')
@category('work')
@input_file('prm_to_lk', 'PVE_96953')
def test_card_creator_in_lk(data):
    """
    Verify Card creator in Leankit
    """
    PRM().Project(data.proj_name, lk_flag=True) \
        .run_integration() \
        .goto_prm().Project(data.proj_name).verify_lk_url() \
        .goto_lk().Card(data.proj_name).verify_creator(data.lk_const.user_name)
