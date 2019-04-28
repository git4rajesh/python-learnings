import pytest
from entities.project.project import Project
from entities.rollups.project import Project as Rollups_Project
from core.src.custom_annotations import tags

@tags('smoke')
def test_project_rollups_html(request):
    project = Project(request)
    project_obj = project.create()
    project_id = project_obj.project_id

    rollups_proj = Rollups_Project(request, project_id)
    html_parsed_to_dct = rollups_proj.get_actual()
    assert html_parsed_to_dct





