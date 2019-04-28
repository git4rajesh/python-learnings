import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../..')
sys.path.extend([path])

from automation.core.src.test_details import zid, input_file, category
from automation.fluent_ml.prm.atoms.artifact import PRM


@zid('98482')
@category('work')
def test_prm_name():
    """
    Work Name: PRM Work Name should be synced as Leankit Card Title on Project Sync
    """
    PRM().Project('Auto_Project_98482', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98482').verify_title('Auto_Project_98482')


@zid('98483')
@category('work')
@input_file('data_title', 'PVE_98483')
def test_title_with_special_character(data):
    """
    Sync Work Name with special characters
    """
    PRM().Project(data.name_with_special_character, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card(data.name_with_special_character).verify_title(data.name_with_special_character)


@zid('98484')
@category('work')
@input_file('data_title', 'PVE_98484')
def test_title_with_numbers(data):
    """
    Sync Work Name with Numbers
    """
    PRM().Project(data.name_with_numbers, lk_flag=True) \
        .run_integration() \
        .goto_lk().Card(data.name_with_numbers).verify_title(data.name_with_numbers)


@zid('98485')
@category('work')
@input_file('data_title', 'PVE_98485')
def test_update_card_title_with_special_character(data):
    """
    Update synced card Title with special characters in Leankit and sync again
    """
    PRM().Project('Auto_Project_98485', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98485').update_title(data.title_with_special_character) \
        .run_integration() \
        .goto_prm().Project(data.title_with_special_character).verify_name(data.title_with_special_character) \
        .goto_lk().Card(data.title_with_special_character).verify_title(data.title_with_special_character)


@zid('98486')
@category('work')
@input_file('data_title', 'PVE_98486')
def test_update_card_title_with_numbers(data):
    """
    Update synced card Title with Numbers in Leankit and sync again
    """
    PRM().Project('Auto_Project_98486', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98486').update_title(data.title_with_numbers) \
        .run_integration() \
        .goto_prm().Project(data.title_with_numbers).verify_name(data.title_with_numbers) \
        .goto_lk().Card(data.title_with_numbers).verify_title(data.title_with_numbers)


@zid('98487')
@category('work')
@input_file('data_title', 'PVE_98487')
def test_update_card_title_with_max_length(data):
    """
    Update synced card Title with max characters(255) in Leankit and sync again
    """
    PRM().Project('Auto_Project_98487', lk_flag=True) \
        .run_integration() \
        .goto_lk().Card('Auto_Project_98487').update_title(data.title_with_max_characters) \
        .run_integration() \
        .goto_prm().Project(data.truncated_title).verify_truncated_name(data.truncated_title) \
        .goto_lk().Card(data.title_with_max_characters).verify_title(data.title_with_max_characters)


@zid('98488')
@category('work')
def test_update_prm_project_name():
    """
    Update synced Project Name in PRM and sync again
    """
    PRM().Project('Auto_Project_98488', lk_flag=True) \
        .run_integration() \
        .goto_prm().Project('Auto_Project_98488').update_name('Updated_Auto_Project_98488') \
        .run_integration() \
        .goto_prm().Project('Auto_Project_98488').verify_name('Auto_Project_98488') \
        .goto_lk().Card('Auto_Project_98488').verify_title('Auto_Project_98488')

