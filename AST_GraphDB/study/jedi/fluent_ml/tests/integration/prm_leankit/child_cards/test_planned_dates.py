import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_CC_Planned_Dates'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True)\
        .run_integration()


@zid('97504')
@category('work')
@input_file('data_planned_dates', 'PVE_97504')
def test_earliest_planned_start_latest_planned_finish(data):
    """
    In LK create cards with planned start date and planned finish date to verify "LK Earliest Planned Start" and "LK Latest Planned Finish" in PRM
    """
    PRM().Project(prm_module_project) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1_97504', 'C2_97504'])\
                .goto_card('C1_97504').set_planned_start(data.c1_planned_start).set_planned_finish(data.c1_planned_finish).update()\
                .goto_card('C2_97504').set_planned_start(data.c2_planned_start).set_planned_finish(data.c2_planned_finish).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_earliest_planned_start(data.c2_planned_start)\
                             .verify_lk_latest_planned_finish(data.c1_planned_finish)


@zid('97505')
@category('work')
@input_file('data_planned_dates', 'PVE_97505')
def test_updated_earliest_planned_start_latest_planned_finish(data):
    """
    In LK Update planned start date and planned finish date to verify "LK Earliest Planned Start" and "LK Latest Planned Finish" in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1_97505', 'C2_97505'])\
                  .goto_card('C1_97505').set_planned_start(data.c1_planned_start).set_planned_finish(data.c1_planned_finish).update()\
                  .goto_card('C2_97505').set_planned_start(data.c2_planned_start).set_planned_finish(data.c2_planned_finish).update()\
        .run_integration()\
        .goto_lk().Card('C2_97505').set_planned_start(data.updated_c2_planned_start).update()\
                  .goto_card('C1_97505').set_planned_finish(data.updated_c1_planned_finish).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_earliest_planned_start(data.c1_planned_start)\
                                                .verify_lk_latest_planned_finish(data.updated_c1_planned_finish)


@zid('97560')
@category('work')
@input_file('data_planned_dates', 'PVE_97560')
def test_earliest_planned_start_latest_planned_finish_after_card_deletion(data):
    """
    In LK Delete one of the child cards with planned start date and planned finish date to verify if "LK Earliest Planned Start" and "LK Latest Planned Finish" is updated in PRM
    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).create_multiple_child_cards(['C1_97560', 'C2_97560'])\
                  .goto_card('C1_97560').set_planned_start(data.c1_planned_start).set_planned_finish(data.c1_planned_finish).update()\
                  .goto_card('C2_97560').set_planned_start(data.c2_planned_start).set_planned_finish(data.c2_planned_finish).update()\
        .run_integration()\
        .goto_lk().Card('C1_97560').delete()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_earliest_planned_start(data.c2_planned_start)\
                                                .verify_lk_latest_planned_finish(data.c2_planned_finish)


@zid('97561')
@category('work')
@input_file('data_planned_dates', 'PVE_97561')
def test_earliest_planned_start_latest_planned_finish_after_removing_dates(data):
    """
     In LK remove planned start date and planned finish date from child to verify
     "LK Earliest Planned Start" and "LK Latest Planned Finish" in PRMcard

    """
    PRM().Project(prm_module_project)\
        .run_integration(skip=True) \
        .goto_lk().Card('C1_97561').set_planned_start(data.c1_planned_start).set_planned_finish(data.c1_planned_finish).update() \
        .run_integration()\
        .goto_lk().Card('C1_97561').unset_planned_start().unset_planned_finish().update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project).verify_lk_earliest_planned_start('')\
                                                .verify_lk_latest_planned_finish('')
