import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../..')
sys.path.extend([path])

from automation.core.src.environment import Environment
from automation.fluent_ml.src import integrator
from automation.integration.src.constants_reader import ConstantsReader


class PRM:
    def __init__(self):
        self.env = Environment()
        self.prm_constants = ConstantsReader.pve_json_const

    def run_integration(self, skip=False, integration_type='default'):
        if not skip:
            integrator.start_integration(integration_type)
        # ToDo Make it to a list
            if (integration_type == 'default' or integration_type == 'card_recreate_enabled'):
                # Condition for the field in ini config file.
                # Only when card is created on running integration, we need this logic
                integrator.update_lk_details_in_ds()
        return self

    def goto_lk(self):
        from automation.fluent_ml.leankit.atoms.artifact import Leankit
        return Leankit()

    def goto_prm(self):
        return self

    def Project(self, name=None, lk_flag=False):
        from automation.fluent_ml.prm.atoms.project import ProjectAtom
        return ProjectAtom(name, lk_flag)

    def MultipleProjects(self, lst_prj_names, lk_flag=False):
        from automation.fluent_ml.prm.atoms.project import ProjectAtom
        return ProjectAtom().create_multiple_projects(lst_prj_names, lk_flag)

    def ProjectWithDescription(self, name, description, lk_flag=False):
        from automation.fluent_ml.prm.atoms.project import ProjectAtom
        return ProjectAtom().create_with_description(name, description, lk_flag)


