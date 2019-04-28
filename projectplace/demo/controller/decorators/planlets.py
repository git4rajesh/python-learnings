class Decorators_Planlets:
    base_url = 'https://rnd3.demo.projectplace.com/api/v1'
    base_url2 = 'https://rnd3.demo.projectplace.com/api/v2'

    def construct_url(self, func):
        def url_wrapper(*args, **kwargs):
            print('Func name ', func.__name__)
            self.complete_url = Decorators_Planlets.base_url + '/planlets/' + func.__name__
            return func(*args, **kwargs)
        return url_wrapper

    def construct_payload(self, create_func):
        def create_payload(*args, **payload):
            self.payload = {
                     'project_id': payload['payload_key']['project_id'],
                     'data':
                         [
                            payload['payload_key']
                         ]
                     }

            return create_func(*args, **payload)

        return create_payload

    def read_url(self, read_func):
        def read_wrapper(*args, **data):
            planlet_id = data['planlet_id']
            project_id = data['project_id']
            self.complete_read_url = Decorators_Planlets.base_url2 + '/planlets/' + str(planlet_id) + '?project_id=' + str(project_id)
            return read_func(*args, **data)

        return read_wrapper