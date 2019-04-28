from entities.rollups.scope import Scope
from entities.rollups.project import Project


class RollupFactory:
    @staticmethod
    def get_rollup_entity(request, parent_type, task_id, project_id):
        """
        This method is used to create the object based on the parent_type
        :param request:
        :param parent_type:
        :param task_id:
        :param project_id:
        :return:
        """
        if parent_type == 'task':
            parent_id = RollupFactory.get_parent_id(request, parent_type, task_id)
            rollup_entity = Scope(request, parent_id, project_id)
        elif parent_type == 'project':
            rollup_entity = Project(request, project_id)
        return rollup_entity

    @staticmethod
    def get_parent_id(request, parent_type, task_id):
        """
        Get the parent id for the lowest hierarchy which is child task
        for the the given parent type
        :param request: pytest request fixture
        :param parent_type: project or scope
        :param task_id: child task_id
        :return: parent_id
        """
        db_store = request.getfixturevalue('tiny_db_store')
        task_details = db_store.search_by_key('task', 'id', task_id)
        temp_parent_id = task_details[0]['parentId']['value']
        temp_parent_type = task_details[0]['parentId']['type']
        if temp_parent_type.lower() != parent_type.lower():
            return task_id
        else:
            task_id = RollupFactory.get_parent_id(request, parent_type, temp_parent_id)
        return task_id


        # parent_id = data_store.search.get_parent_id(parent_type, 'task', task_id, data_store.get())
        # for task in task_details:
        #     if parent_type == task['parentId']['type']:
        #

