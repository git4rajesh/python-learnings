import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_Planned_Dates'


def module_setup():
    PRM().Project(prm_module_project, lk_flag=True).run_integration()


@zid('97710')
@category('work')
@input_file('data_planned_dates', 'PVE_97710')
def test_planned_start_planned_finish(data):
    """
    PRM-LK: Verify LK Planned Start, LK Planned Finish field
    """
    PRM().Project(prm_module_project, lk_flag=True) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project) \
                         .set_planned_start(data.planned_start)\
                         .set_planned_finish(data.planned_finish).update()\
        .run_integration()\
        .goto_prm().Project(prm_module_project) \
                             .verify_lk_planned_start(data.planned_start)\
                             .verify_lk_planned_finish(data.planned_finish)


@zid('97706')
@category('work')
@input_file('data_planned_dates', 'PVE_97706')
def test_scheduled_start_scheduled_finish(data):
    """
    PRM-LK: Verify LK Planned Start, LK Planned Finish fields when PRM project has schedule start and schedule finish
    """
    PRM().Project(data.name, lk_flag=True) \
                   .update_scheduled_start_and_finish(data.scheduled_start, data.scheduled_finish)\
        .run_integration() \
        .goto_lk().Card(data.name).verify_planned_start(data.scheduled_start)\
                         .verify_planned_finish(data.scheduled_finish)\
        .goto_prm().Project(data.name).verify_lk_planned_start(data.scheduled_start)\
                             .verify_lk_planned_finish(data.scheduled_finish)\



@zid('97712')
@category('work')
@input_file('data_planned_dates', 'PVE_97712')
def test_updated_planned_start_planned_finish(data):
    """
    PRM-LK: Update Planned Start and Planned Finish for a synced card in Leankit and sync again
    """
    PRM().Project(data.name, lk_flag=True) \
                   .update_scheduled_start_and_finish(data.prm_scheduled_start, data.prm_scheduled_finish)\
        .run_integration() \
        .goto_lk().Card(data.name).set_planned_start(data.lk_planned_start)\
                         .set_planned_finish(data.lk_planned_finish).update()\
        .run_integration()\
        .goto_prm().Project(data.name).verify_lk_planned_start(data.lk_planned_start)\
                             .verify_lk_planned_finish(data.lk_planned_finish)\
        .goto_lk().Card(data.name).verify_planned_start(data.lk_planned_start)\
                         .verify_planned_finish(data.lk_planned_finish)