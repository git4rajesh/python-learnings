from string import Template

from automation.xml_utils import sax_utils
from automation.pve.src import constants
from automation.fluent_ml.prm.features.artifact import Artifact


class QuerySvc(Artifact):
    def __init__(self):
        super().__init__()
        template = Template(constants.QUERY_WSDL)
        self.soap_wsdl = template.substitute(protocol=self.env.pve.protocol, pve_env=self.env.pve.name)

    def read(self, *args):
        query_params = args
        payload = self._prepare_payload(query_params)
        response = self.get_read_response(payload, encoding='utf-8')
        db_rows = self._convert_xml_response_to_db_rows(response.text)
        return db_rows

    def read_as_dict(self, query, params, result_node='e:ArrayOfanyType', column_node='d:ColumnNames'):
        query_params = [query, params]
        payload = self._prepare_payload(query_params)
        response = self.get_read_response(payload, encoding='utf-8')

        return self._convert_xml_response_to_dict(response.text, result_node, column_node)

    def _convert_xml_response_to_dict(self, response, result_node, column_node):
        dct = self.parse_wrapper.get_response_dict(response, result_node, column_node)
        return dct

    @staticmethod
    def _prepare_payload(query_params):
        final_query = QuerySvc._substitute_params_in_query(query_params)
        payload = {'sqlQuery': final_query}
        return payload

    @staticmethod
    def _substitute_params_in_query(query_params):

        length = len(query_params)

        if length == 1:
            query = query_params[0]
            query = QuerySvc._escape_xml_chars(query)
        elif length == 2:
            query, params = query_params
            query = QuerySvc._escape_xml_chars(query)
            params = QuerySvc._escape_params(params)
            query = query % params
        else:
            query = None
        return query

    @staticmethod
    def _escape_xml_chars(string):
        if string:
            if sax_utils.should_escape_xml_string(string, sax_utils.XML_INVALID_CHARS):
                string = sax_utils.escape_xml_string(string)

        return string

    def get_read_response(self, payload, encoding='utf-8'):
        """
        internal function
        :param payload: request for read query
        :return: response from the read query service
        """
        try:
            response = self._call_api(payload, encoding)
        except WindowsError:
            # Temp fix to work Query service with Http
            self.soap_wsdl = self.soap_wsdl.replace('https', 'http')
            response = self._call_api(payload, encoding)
        return response

    def _convert_xml_response_to_db_rows(self, response):
        db_rows = self.parse_wrapper.get_nested_values(response)
        return db_rows

    def _call_api(self, payload, encoding):
        # query service uses read operation for all CRUD operations
        soap_action, soap_payload = self.payload_gen.get_soap_details('query', 'read', payload)
        soap = self.initialize_soap_request(self.cert, soap_payload, soap_action)

        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        return response

    @staticmethod
    def _escape_params(params):
        if isinstance(params, tuple):
            param_list = list(params)
            escaped = []

            for param in param_list:
                invalid_char_escaped = QuerySvc._escape_xml_chars(param)
                invalid_quote_escaped = QuerySvc._escape_xml_quotes(invalid_char_escaped)
                escaped.append(invalid_quote_escaped)

            params = tuple(escaped)

        return params

    @staticmethod
    def _escape_xml_quotes(string):
        if string:
            if sax_utils.should_escape_xml_string(string, sax_utils.XML_INVALID_QUOTES):
                string = sax_utils.escape_quotes(string)

        return string
