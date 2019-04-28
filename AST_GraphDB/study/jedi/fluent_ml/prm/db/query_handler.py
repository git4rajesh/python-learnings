from automation.fluent_ml.prm.features.query_svc import QuerySvc

from automation.fluent_ml.prm.db import queries


class QueryHandler:
    def __init__(self):
        self.query_svc = QuerySvc()

    def select_external_id(self, project_id):
        query = queries.SELECT_XID
        params = project_id
        result = self.query_svc.read(query, params)
        return result[0][0] if result else None

    def select_project_details(self, project_id):
        query = queries.SELECT_PROJECT_DETAILS
        params = project_id
        result = self.query_svc.read_as_dict(query, params)
        return result

    def select_project_description(self, project_id):
        query = queries.SELECT_PROJECT_DESCRIPTION
        params = project_id
        result = self.query_svc.read(query, params)
        return result

    def select_project_name(self, project_id):
        query = queries.SELECT_PROJECT_NAME
        params = project_id
        result = self.query_svc.read(query, params)
        return result[0][0] if result else result