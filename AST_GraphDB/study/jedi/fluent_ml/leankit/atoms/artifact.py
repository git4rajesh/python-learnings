import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../..')
sys.path.extend([path])

from automation.fluent_ml.src import integrator
from automation.integration.src.constants_reader import ConstantsReader


class Leankit:
    def __init__(self):
        self.lk_constants = ConstantsReader.lk_json_const

    def goto_lk(self):
        return self

    def goto_prm(self):
        from automation.fluent_ml.prm.atoms.artifact import PRM
        return PRM()

    def Card(self, name, board='board1'):
        from automation.fluent_ml.leankit.atoms.card import CardAtom
        return CardAtom(name, board)

    def Board(self):
        from automation.fluent_ml.leankit.atoms.board import BoardAtom
        return BoardAtom()

    def run_integration(self, skip=False, integration_type='default'):
        if not skip:
            integrator.start_integration(integration_type)
            # ToDo Make it to a list
            if (integration_type == 'default' or integration_type == 'card_recreate_enabled'):
                # Condition for the field in ini config file.
                # Only when card is created on running integration, we need this logic
                integrator.update_lk_details_in_ds()
        return self
