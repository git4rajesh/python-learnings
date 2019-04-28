import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM

prm_module_project = 'Auto_Module_Description'
description = 'Module Project Description'


def module_setup():
    PRM().ProjectWithDescription(prm_module_project, description, lk_flag=True).run_integration()


@zid('97154')
@category('work')
@input_file('data_description', 'PVE_97154')
def test_prm_description(data):
    """
    Work Description: PRM Work Description should be synced as Leankit Card Description on Project Sync
    """
    PRM().ProjectWithDescription('Auto_Project_97154', data.description, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_97154').verify_description(data.description)


@zid('97155')
@category('work')
@input_file('data_description', 'PVE_97155')
def test_update_description_in_lk(data):
    """
    Work Description: Update synced card description in Leankit and sync again
    """
    PRM().ProjectWithDescription(prm_module_project, description) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).update_description(data.new_description) \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_description(data.new_description)


@zid('97156')
@category('work')
@input_file('data_description', 'PVE_97156')
def test_update_description_in_prm(data):
    """
    Work Description: Update synced project work description in PRM and sync again
    """
    PRM().ProjectWithDescription('Auto_Project_97156', data.description, lk_flag=True) \
        .run_integration() \
        .goto_prm().Project('Auto_Project_97156').update_description(data.new_description) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_97156').verify_description(data.description) \
        .goto_prm().Project('Auto_Project_97156').verify_description(data.description)


@zid('97157')
@category('work')
def test_delete_description_in_lk():
    """
     Work Description: Delete synced card description in Leankit and sync again
    """
    PRM().ProjectWithDescription('Auto_Project_97157', '97157_Project_Description', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_97157').delete_description() \
        .run_integration() \
        .goto_prm().Project('Auto_Project_97157').verify_description('')


@zid('97158')
@category('work')
@input_file('data_description', 'PVE_97158')
def test_description_with_special_characters(data):
    """
     Work Description: Sync Work Description with special characters
    """
    PRM().ProjectWithDescription('Auto_Project_97158', data.special_character_description, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_97158').verify_description(data.special_character_description)


@zid('97159')
@category('work')
@input_file('data_description', 'PVE_97159')
def test_update_description_with_special_characters(data):
    """
    Work Description: Update synced card description with special characters in Leankit and sync again
    """
    PRM().ProjectWithDescription(prm_module_project, description) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).update_description(data.special_character_description) \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_description(data.special_character_description)


@zid('97160')
@category('work')
@input_file('data_description', 'PVE_97160')
def test_update_description_with_numbers(data):
    """
    Work Description: Update synced card description with numbers in Leankit and sync again
    """
    PRM().ProjectWithDescription(prm_module_project, description) \
        .run_integration(skip=True) \
        .goto_lk().Card(prm_module_project).update_description(data.numeric_description) \
        .run_integration() \
        .goto_prm().Project(prm_module_project).verify_description(data.numeric_description)


@zid('97161')
@category('work')
@input_file('data_description', 'PVE_97161')
def test_description_with_numbers(data):
    """
    Work Description: Sync Work Description with numbers
    """
    PRM().ProjectWithDescription('Auto_Project_97161', data.numeric_description, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_97161').verify_description(data.numeric_description)


@zid('98359')
@category('work')
@input_file('data_description', 'PVE_98359')
def test_description_with_max_characters(data):
    """
     Work Description: set work description with more than 20000 characters and sync again
     BUG : PVE-98475
     NOTE: This test is failing as integration allows more than 20k characters for leankit description
    """
    PRM().ProjectWithDescription('Auto_Project_98359', data.desc_with_max_characters, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98359').verify_description(data.truncated_desc)