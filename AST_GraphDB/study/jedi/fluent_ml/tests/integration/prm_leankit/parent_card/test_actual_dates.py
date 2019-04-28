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


@zid('98057')
@category('work')
def test_actual_start_finish_dates_for_completed_card():
    """
    Verify LK Actual Start, LK Actual Finish fields for a Completed Card
    """

    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_lane('completed').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project)\
                            .verify_lk_actual_start()\
                            .verify_lk_actual_finish()


@zid('98058')
@category('work')
def test_actual_start_date_for_in_process_card():
    """
    Verify LK Actual Start Field for a in process card
    """

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_lane('in_process').update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_actual_start()


@zid('98059')
@category('work')
def test_actual_start_finish_dates_for_in_process_card():
    """
    Verify LK Actual Start and Finish Fields when a synced card is moved from "Completed" to "In Process" Lane
    """

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).set_lane('completed').update() \
        .run_integration() \
        .goto_lk().Card(prm_module_project).set_lane('in_process').update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project)\
                           .verify_lk_actual_start()\
                           .verify_lk_actual_finish()


@zid('98060')
@category('work')
def test_card_moved_to_connected_cards_done_lane():
    """
    PRM-LK: Verify LK Actual Start and LK Actual Finish fields when a synced card is moved to a Lane which is
    set with "Connected Cards Done Lane"
    """
    PRM().Project('Auto_Project_98060', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98060').move_to_board(board='board2') \
                         .move_to_connected_cards_done_lane()\
        .run_integration() \
        .goto_prm().Project('Auto_Project_98060').verify_lk_actual_start()\
                             .verify_lk_actual_finish()
