import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_CC_Actual_Dates'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration()


@zid('97563')
@category('work')
def test_actual_dates_for_child_card_in_process():
    """
    In LK move a child card to "in progress" lane and verify "LK Earliest Actual Start" in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                  .goto_card('C1').set_lane('in_process').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_earliest_actual_start() \
                                               .verify_lk_latest_actual_finish()


@zid('97564')
@category('work')
def test_actual_dates_for_child_card_complete():
    """
    In LK move a child card to "complete" lane and verify "LK Earliest Actual Start" and "LK Latest Actual Finish" in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
        .goto_card('C1').set_lane('completed').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_earliest_actual_start() \
                                               .verify_lk_latest_actual_finish()


@zid('98294')
@category('work')
def test_actual_dates_for_child_cards_in_different_status():
    """
     In LK create 2 child cards in "in progress" and "complete lane respectively and verify "LK Earliest Actual Start"
     and "LK Latest Actual Finish" in PRM
     Fails as Card read API in Leankit returns the completed card date only if both the cards are in completed state
     Need clarity on the behaviour.
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                  .goto_card('C1').set_lane('in_process').update() \
                  .goto_card('C2').set_lane('completed').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_earliest_actual_start() \
                                                .verify_lk_latest_actual_finish()


@zid('97588')
@category('work')
def test_actual_dates_for_deleted_child_cards():
    """
    In LK delete child card in "complete" lane and verify "LK Earliest Actual Start" and "LK Latest Actual Finish" in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                  .goto_card('C1').set_lane('completed').update() \
        .run_integration() \
        .goto_lk().Card('C1').delete() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_earliest_actual_start() \
                                                .verify_lk_latest_actual_finish()
