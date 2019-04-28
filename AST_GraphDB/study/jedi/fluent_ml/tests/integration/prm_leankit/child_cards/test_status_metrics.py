import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_CC_Status'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True)\
        .run_integration()


@zid('97447')
@category('work')
def test_child_cards_status_metrics():
    """Create child cards of different status in Leankit and verify LK Cards Total in PRM"""

    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3']) \
                .goto_card('C1').set_lane('not_started').set_size(10).update() \
                .goto_card('C2').set_lane('in_process').set_size(15).update() \
                .goto_card('C3').set_lane('completed').set_size(25).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(50)\
                             .verify_lk_not_started_child_cards(10)\
                             .verify_lk_in_process_child_cards(15)\
                             .verify_lk_completed_child_cards(25)\
                             .verify_lk_percent_of_cards_completed(50)


@zid('97449')
@category('work')
def test_total_child_cards():
    """Add Child cards in Leankit and verify "LK Cards Total" in PRM"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                .goto_card('C1').set_lane('not_started').set_size(10).update() \
        .run_integration() \
        .goto_lk().Card(prm_module_project).create_child_card('C2') \
                .goto_card('C2').set_lane('completed').set_size(10).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(20)


@zid('97450')
@category('work')
def test_not_started_child_cards():
    """Create Child cards in Leankit and verify "LK Not started Child card" in PRM"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('not_started').set_size(25).update() \
                .goto_card('C2').set_lane('not_started').set_size(15).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_not_started_child_cards(40)


@zid('97451')
@category('work')
def test_in_process_child_cards():
    """Create child cards in Leankit and verify "LK In Process Child card" in PRM"""

    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('in_process').set_size(25).update() \
                .goto_card('C2').set_lane('in_process').set_size(15).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_in_process_child_cards(40)


@zid('97452')
@category('work')
def test_completed_child_cards():
    """Create child cards in Leankit and verify "LK Completed Child card" in PRM"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('completed').set_size(25).update() \
                .goto_card('C2').set_lane('completed').set_size(25).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_completed_child_cards(50)


@zid('97453')
@category('work')
def test_not_started_child_cards_after_deletion():
    """Delete one of the Not started child cards in Leankit"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('not_started').set_size(20).update() \
                .goto_card('C2').set_lane('not_started').set_size(10).update() \
        .run_integration() \
        .goto_lk().Card('C2').delete() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_not_started_child_cards(20)\
                             .verify_lk_total_cards(20)


@zid('97454')
@category('work')
def test_in_process_child_cards_after_deletion():
    """Delete one of the In Process child cards in Leankit"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('in_process').set_size(20).update() \
                .goto_card('C2').set_lane('in_process').set_size(10).update() \
        .run_integration() \
        .goto_lk().Card('C2').delete() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_in_process_child_cards(20)\
                                                .verify_lk_total_cards(20)


@zid('97455')
@category('work')
def test_completed_child_cards_after_deletion():
    """Delete one of the Completed child cards in Leankit"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2']) \
                .goto_card('C1').set_lane('completed').set_size(20).update() \
                .goto_card('C2').set_lane('completed').set_size(10).update() \
        .run_integration() \
        .goto_lk().Card('C2').delete() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_completed_child_cards(20)\
                                                .verify_lk_total_cards(20)


@zid('97456')
@category('work')
def test_child_cards_status_metrics_after_deletion():
    """Delete child cards of different status in Leankit and verify LK Cards Total in PRM"""

    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3']) \
                .goto_card('C1').set_lane('not_started').set_size(10).update() \
                .goto_card('C2').set_lane('in_process').set_size(15).update() \
                .goto_card('C3').set_lane('completed').set_size(25).update() \
        .run_integration() \
        .goto_lk().Card('C1').delete()\
                .goto_card('C2').delete()\
                .goto_card('C3').delete() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(0)\
                             .verify_lk_not_started_child_cards(0 )\
                             .verify_lk_in_process_child_cards(0)\
                             .verify_lk_completed_child_cards(0)\
                             .verify_lk_percent_of_cards_completed(0)


@zid('97497')
@category('work')
def test_child_cards_status_metrics_after_size_update():
    """Update the size of child cards (of different status) in Leankit"""

    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3']) \
                .goto_card('C1').set_lane('not_started').set_size(5).update() \
                .goto_card('C2').set_lane('in_process').set_size(15).update() \
                .goto_card('C3').set_lane('completed').set_size(25).update() \
        .run_integration() \
        .goto_lk().Card('C1').set_size(10).update() \
                .goto_card('C2').set_size(10).update() \
                .goto_card('C3').set_size(10).update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(30)\
                                                .verify_lk_not_started_child_cards(10 )\
                                                .verify_lk_in_process_child_cards(10)\
                                                .verify_lk_completed_child_cards(10)\
                                                .verify_lk_percent_of_cards_completed(33.0)


@zid('97494')
@category('work')
def test_status_update_to_inprocess():
    """
    PRM-LK Integ - Update child card status from Not Started to In Process in Leankit
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                .goto_card('C1').set_size(5).set_lane('not_started').update() \
        .run_integration() \
        .goto_lk().Card('C1').set_lane('in_process').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(5)\
                             .verify_lk_not_started_child_cards(0)\
                             .verify_lk_in_process_child_cards(5)


@zid('97495')
@category('work')
def test_status_update_to_completed():
    """
    PRM-LK Integ - Update child card status from Not Started to Completed in Leankit
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                .goto_card('C1').set_lane('not_started').set_size(15).update() \
        .run_integration() \
        .goto_lk().Card('C1').set_lane('completed').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(15)\
                             .verify_lk_not_started_child_cards(0)\
                             .verify_lk_completed_child_cards(15)\
                             .verify_lk_percent_of_cards_completed(100.0)


@zid('97496')
@category('work')
def test_status_update_from_complete_to_inprocess():
    """
    PRM-LK Integ - Update child card status from Completed to In Process in Leankit
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1') \
                .goto_card('C1').set_lane('completed').set_size(20).update() \
        .run_integration() \
        .goto_lk().Card('C1').set_lane('in_process').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(20)\
                             .verify_lk_in_process_child_cards(20)\
                             .verify_lk_completed_child_cards(0)\
                             .verify_lk_percent_of_cards_completed(0)


@zid('98542')
@category('work')
def test_child_card_metrics_when_child_cards_created_in_different_boards():
    """
    In Leankit Create child cards in multiple board and verify LK Cards Total in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3'], board='board1')\
                                           .create_multiple_child_cards(['C4', 'C5', 'C6'], board='board2')\
                  .goto_card('C1', board='board1').set_lane('not_started').update() \
                  .goto_card('C2', board='board1').set_lane('in_process').update() \
                  .goto_card('C3', board='board1').set_lane('completed').update() \
                  .goto_card('C4', board='board2').set_lane('not_started').update() \
                  .goto_card('C5', board='board2').set_lane('in_process').update() \
                  .goto_card('C6', board='board2').set_lane('completed').update() \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_lk_total_cards(6) \
                             .verify_lk_not_started_child_cards(2) \
                             .verify_lk_in_process_child_cards(2)\
                             .verify_lk_completed_child_cards(2)\
                             .verify_lk_percent_of_cards_completed(33.00)