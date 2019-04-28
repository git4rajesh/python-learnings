import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM


@zid('97705')
@category('work')
def test_top_lane_field():
    """
    Verify LK Top Lane field in PRM
    """
    PRM().Project('Auto_97705', lk_flag=True) \
        .run_integration() \
        .goto_prm().Project('Auto_97705').verify_default_lk_top_lane() \
        .goto_lk().Card('Auto_97705').verify_default_top_lane()
