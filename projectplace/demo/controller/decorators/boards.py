from datetime import datetime


class Decorators_Board:
    base_url = 'https://rnd3.demo.projectplace.com/api/v1'

    def create_payload(self, create_func):
        def create_wrapper(*args, **kwargs):
            self.board_name = Decorators_Board.generate_name(args[0].board_name)
            self.payload = {
                "name": self.board_name
            }
            return create_func(*args, **kwargs)

        return create_wrapper

    def create_url(self, create_func):
        def create_wrapper(*args, **kwargs):
            workspace_id = args[1]
            self.complete_create_url = Decorators_Board.base_url + '/projects/' + str(workspace_id) + '/boards/create-new'
            return create_func(*args, **kwargs)
        return create_wrapper

    def read_delete_update_url(self, func):
        def inner_func(*payload, **kwargs):
            board_id = payload[1]
            self.complete_url = Decorators_Board.base_url + '/boards/' + str(board_id)
            return func(*payload, **kwargs)
        return inner_func

    @staticmethod
    def generate_name(project_name):
        timestamp = str(datetime.now()).replace(' ', '_').replace('.', '_')
        name = 'Auto_%(name)s_%(timestamp)s' % {'name': project_name,
                                                'timestamp': timestamp}
        return name

