import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../../../../..')
sys.path.extend([path])

from automation.fluent_ml.src import helper

desc_with_numbers = helper.get_description_with_numbers(4000)
desc_with_characters = helper.get_description_with_characters(4000)
new_desc_with_characters = helper.get_description_with_characters(4000)
desc_with_special_characters = helper.get_description_with_special_characters(4000)
desc_with_max_characters = helper.get_description_with_characters(24000)

PVE_97154 = {'description': desc_with_characters}

PVE_97155 = {'description': desc_with_characters, 'new_description': new_desc_with_characters}

PVE_97156 = {'description': desc_with_characters, 'new_description': desc_with_numbers}

PVE_97158 = {'special_character_description': desc_with_special_characters}

PVE_97159 = {'special_character_description': desc_with_special_characters}

PVE_97160 = {'numeric_description': desc_with_numbers}

PVE_97161 = {'numeric_description': desc_with_numbers}


PVE_98359 = {'desc_with_max_characters': desc_with_max_characters, 'truncated_desc': desc_with_max_characters[0:20000]}