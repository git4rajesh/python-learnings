import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../../..')
sys.path.extend([path])

from automation.fluent_ml.src import helper

name_with_numbers = helper.get_description_with_numbers(50)
name_with_special_characters = helper.get_description_with_special_characters(50)
name_with_max_characters = helper.get_description_with_characters(255)

PVE_98483 = {'name_with_special_character': name_with_special_characters}

PVE_98484 = {'name_with_numbers': name_with_numbers}

PVE_98485 = {'title_with_special_character': name_with_special_characters}

PVE_98486 = {'title_with_numbers': name_with_numbers}

PVE_98487 = {'title_with_max_characters': name_with_max_characters, 'truncated_title': name_with_max_characters[0:50]}
