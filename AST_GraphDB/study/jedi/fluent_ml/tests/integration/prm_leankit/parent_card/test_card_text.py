import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_Card_Text'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration()


@zid('98489')
@category('work')
def test_card_text_field():
    """
    Verify LK Card Text field on project sync
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_prm().Project(prm_module_project).verify_lk_card_text()


@zid('98490')
@category('work')
def test_card_link_url():
    """
    Verify LK Card field on project sync
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_prm().Project(prm_module_project).verify_lk_url()
