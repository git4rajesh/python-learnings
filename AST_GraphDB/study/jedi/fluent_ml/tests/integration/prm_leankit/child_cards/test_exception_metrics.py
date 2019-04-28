import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_CC_Exception_Count'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration()\
        .goto_lk().Card(prm_module_project).set_size(10).update()


@zid('98169')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_exception_metrics_when_multiple_child_cards(data):
    """
    In LK add exceptions to multiple child cards and verify "LK Exception Count"
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3', 'C4'])\
                         .goto_card('C1').set_planned_start(data.past_start_date).update()\
                         .goto_card('C2').set_planned_finish(data.past_finish_date).update()\
                         .goto_card('C3').set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(1)\
                             .verify_lk_missed_finish_child_cards(1)\
                             .verify_lk_blocked_child_cards(1)\
                             .verify_lk_exception_count(2)\
                             .verify_lk_exception_percent(50)


@zid('97589')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_start_child_card_exception_without_size(data):
    """
    In LK create child card(without size) with past day as planned start date and verify "LK Missed Start Child Cards" in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'])\
                .goto_card('C1').set_planned_start(data.past_start_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(1)\
                                                .verify_lk_exception_count(0)\
                                                .verify_lk_exception_percent(0)


@zid('97696')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_start_child_card_exception_with_size(data):
    """
    In LK create child card(with size) with past day as planned start date and verify "LK Missed Start Child Cards" in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'])\
                         .goto_card('C1').set_size(10).update()\
                         .goto_card('C2').set_size(12).update()\
                         .goto_card('C1').set_planned_start(data.past_start_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(1)\
                                                .verify_lk_exception_count(0)\
                                                .verify_lk_exception_percent(0)


@zid('97700')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_finish_child_card_exception_with_size(data):
    """
    In LK create child card(with size) with past day as planned finish date and verify "LK Missed Finish Child Cards" in PRM
    Note: Currently Exception percentage is calculated as (No of exception cards)/(Total Size of child cards)). This behavior might change
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'])\
                         .goto_card('C1').set_size(5).update()\
                         .goto_card('C2').set_size(5).update()\
                         .goto_card('C1').set_planned_finish(data.past_finish_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_finish_child_cards(1)\
                             .verify_lk_exception_count(1)\
                             .verify_lk_exception_percent(10)


@zid('97697')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_finish_child_card_exception_without_size(data):
    """
    In LK create child card(without size) with past day as planned finish date and verify "LK Missed Finish Child Cards" in PRM	
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'])\
                  .goto_card('C1').set_planned_finish(data.past_finish_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_finish_child_cards(1)\
                             .verify_lk_exception_count(1)\
                             .verify_lk_exception_percent(50)


@zid('97702')
@category('work')
def test_blocked_child_card_exception_with_size():
    """
    In LK block child card(with size) and verify "LK Blocked Child Cards" in PRM
    Note: Currently Exception percentage is calculated as (No of exception cards)/(Total Size of child cards)). This behavior might change
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'])\
                         .goto_card('C1').set_size(20).set_blocked_flag(is_blocked=True).update()\
                         .goto_card('C2').set_size(10).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_blocked_child_cards(1)\
                             .verify_lk_exception_count(1)\
                             .verify_lk_exception_percent(3)


@zid('97703')
@category('work')
@input_file('data_exception_metrics', 'finish_dates')
def test_parent_planned_finish_lesser_than_child_planned_finish(data):
    """
    In LK set parent card's planned finish lesser than child cards planned finish date and verify "LK Exception Count" in PRM
    Note: Currently Exception percentage is calculated as (No of exception cards)/(Total Size of child cards)). This behavior might change
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                         .goto_card('C1').set_size(10)\
                                         .set_planned_finish(data.child_finish_date).update()\
                         .goto_card(prm_module_project).set_planned_finish(data.parent_finish_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_exception_count(1)\
                                                .verify_lk_exception_percent(10)


@zid('97707')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_exception_metrics_when_one_child_card_without_size(data):
    """
    In LK create a child card(without size) with planned start date and end date lesser than current date, block the child card and verify exception count in PRM
    Bug: This test case fails because of bug PVE-97324: "LK Exception count" counts number of exceptions per card instead of number of cards with exception.
    Expected: Exception Count=1, Exception Percentage=100 Actual: Exception Count=2, Exception Percentage=200
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                  .goto_card('C1').set_planned_start(data.past_start_date)\
                                  .set_planned_finish(data.past_finish_date)\
                                  .set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(1)\
                             .verify_lk_missed_finish_child_cards(1)\
                             .verify_lk_blocked_child_cards(1)\
                             .verify_lk_exception_count(1)\
                             .verify_lk_exception_percent(100)


@zid('97708')
@category('work')
@input_file('data_exception_metrics', 'finish_dates')
def test_exception_metrics_when_parent_planned_finish_greater_than_child(data):
    """
    In LK update child card's planned finish date lesser or equal to parent card's planned finish and verify "LK Exception Count" is reset in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                         .goto_card('C1').set_size(10)\
                                         .set_planned_finish(data.child_finish_date).update()\
                         .goto_card(prm_module_project).set_planned_finish(data.parent_finish_date).update()\
        .run_integration()\
        .goto_lk().Card('C1').set_planned_finish(data.parent_finish_date).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_exception_count(0)\
                                                .verify_lk_exception_percent(0)


@zid('97709')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_exception_metrics_when_one_child_card_with_size(data):
    """
    In LK update a child card with planned start date and end date lesser than current date, block the child card and verify exception count in PRM
    Bug: This test case fails because of bug PVE-97324: "LK Exception count" counts number of exceptions per card instead of number of cards with exception.
    Note: Currently Exception percentage is calculated as (No of exception cards)/(Total Size of child cards)). This behavior might change
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                  .goto_card('C1').set_size(10)\
                                  .set_planned_start(data.past_start_date)\
                                  .set_planned_finish(data.past_finish_date)\
                                  .set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(1)\
                                                .verify_lk_missed_finish_child_cards(1)\
                                                .verify_lk_blocked_child_cards(1)\
                                                .verify_lk_exception_count(1)\
                                                .verify_lk_exception_percent(10)


@zid('97711')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_metrics_when_child_cards_with_exceptions_deleted(data):
    """
    In LK add exceptions to multiple child cards and verify "LK Exception Count"
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2', 'C3'])\
                  .goto_card('C1').set_size(5).set_planned_start(data.past_start_date).update()\
                  .goto_card('C2').set_size(10).set_planned_finish(data.past_finish_date).update()\
                  .goto_card('C3').set_size(5).set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_lk().Card('C1').delete()\
                  .goto_card('C2').delete()\
                  .goto_card('C3').delete()\
        .run_integration() \
        .goto_prm().Project(prm_module_project)\
                             .verify_lk_missed_start_child_cards(0)\
                             .verify_lk_missed_finish_child_cards(0)\
                             .verify_lk_blocked_child_cards(0)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)


@zid('98103')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_start_child_card_reset_when_exception_resolved(data):
    """
    In LK resolve 'Missed start child card' exception and verify "LK Missed Start Child Card" is reset in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                  .goto_card('C1').set_planned_start(data.past_start_date).update()\
        .run_integration()\
        .goto_lk().Card('C1').set_planned_start(data.future_start_date).update()\
        .run_integration() \
        .goto_prm().Project(prm_module_project)\
                             .verify_lk_missed_start_child_cards(0)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)


@zid('98336')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_finish_child_card_reset_when_exception_resolved(data):
    """
    In LK resolve 'missed finish child card' exception and verify "LK Missed Finish Child Card" is reset in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                  .goto_card('C1').set_planned_finish(data.past_finish_date).update()\
        .run_integration()\
        .goto_lk().Card('C1').set_planned_finish(data.future_finish_date).update()\
        .run_integration() \
        .goto_prm().Project(prm_module_project)\
                             .verify_lk_missed_finish_child_cards(0)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)


@zid('98337')
@category('work')
def test_blocked_child_card_reset_when_exception_resolved():
    """
    In LK resolve 'blocked child card' exception and verify "LK Blocked Child Card" is reset in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_child_card('C1')\
                  .goto_card('C1').set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_lk().Card('C1').set_blocked_flag(is_blocked=False).update()\
        .run_integration() \
        .goto_prm().Project(prm_module_project)\
                             .verify_lk_blocked_child_cards(0)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)


@zid('98537')
@category('work')
def test_blocked_child_card_exception_with_multiple_cards():
    """
    In LK create multiple child cards, block them and verify "LK Blocked Child Cards" in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'], board='board1')\
                  .goto_card('C1').set_size(20).set_blocked_flag(is_blocked=True).update()\
                  .goto_card('C2').set_size(10).set_blocked_flag(is_blocked=True).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_blocked_child_cards(2)\
                             .verify_lk_exception_count(2)\
                             .verify_lk_exception_percent(7)


@zid('98535')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_start_child_card_exception_with_multiple_cards(data):
    """
     In LK create multiple child cards(with size) with past day as planned start date and verify "LK Missed Start Child Cards" in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'], board='board1') \
                  .goto_card('C1').set_size(20).set_planned_start(data.past_start_date).update() \
                  .goto_card('C2').set_size(10).set_planned_start(data.past_start_date).update() \
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_start_child_cards(2)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)


@zid('98536')
@category('work')
@input_file('data_exception_metrics', 'start_and_finish_dates')
def test_missed_finish_child_card_exception_with_multiple_cards(data):
    """
     In LK create multiple child cards(with size) with planned finish date less than current date and verify "LK Missed Finish Child Cards" in PRM
     BUG: PVE-98476:
     This is test is failing now as exception counts LK Missed Finish where as it should not
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1', 'C2'], board='board1') \
                  .goto_card('C1').set_size(20).set_planned_finish(data.past_finish_date).update() \
                  .goto_card('C2').set_size(10).set_planned_finish(data.past_finish_date).update() \
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_missed_finish_child_cards(2)\
                             .verify_lk_exception_count(0)\
                             .verify_lk_exception_percent(0)