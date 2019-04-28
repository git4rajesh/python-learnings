from demo_module import Demo_Module
from controller.boards import Boards
from controller.planlets import Planlets


class TestAPI:
    def __init__(self):
        pass

    def run_projects(self):
        demo_obj = Demo_Module()
        workspace_id = demo_obj.create_project('MyProject')
        demo_obj.read_projects(workspace_id)
        return workspace_id

        # # demo_obj.set_sync_flag(project_id)
        # # demo_obj.update_project(project_id)
        # # demo_obj.read_projects(project_id)
        # demo_obj.list_projects()
        # demo_obj.call_delete_project()

    def run_boards(self, workspace_id):
        boards_ctrl = Boards(workspace_id, board_name='Board')
        board_id, status = boards_ctrl.create(workspace_id)

        print('>>After Creation', board_id, status)

        payload_update = {'is_archived': 'true', 'name':'updated_board_name'}

        response, status = boards_ctrl.update(board_id, payload_update)
        print('After Updation>>>', status)

        response = boards_ctrl.read(board_id)
        print('>>>>', response.text)

        response, status = boards_ctrl.delete(board_id)
        print('>>>>', response.text, status)

    def run_planlets(self, workspace_id):
        planlets_ctrl = Planlets()
        create_data_dict = {
                        'project_id': workspace_id,
                        'name': 'Planlet1_name',
                        'sort_order': 1,
                        'kind': 0,
                        'description': 'My Planlet1 desc'
                    }
        planlet_id, status = planlets_ctrl.create(payload_key=create_data_dict)

        print('After Create', planlet_id, status)

        update_data_dict = {
            "id": planlet_id,
            "project_id": 251135,
            'kind': 1,
            'name': 'Updated_name',
        }
        updated_planlet_id, status = planlets_ctrl.edit(payload_key=update_data_dict)
        print('After Update', planlet_id, status)


        delete_data_dict = {
            "id": planlet_id,
            "project_id": 251135
        }
        status = planlets_ctrl.delete(payload_key=delete_data_dict)
        print('Deletion status', status)




if __name__ == "__main__":
    test_obj = TestAPI()
    # workspace_id = test_obj.run_projects()
    test_obj.run_planlets(251135)
    # test_obj.run_boards(project_id)
