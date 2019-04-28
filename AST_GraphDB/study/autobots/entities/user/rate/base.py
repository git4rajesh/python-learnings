from core import utils
from core.asserter import Asserter
from core.db import db_wrapper
from core.src.json_generator import PayloadGenerator
from entities.entity import Entity

ENTITY = 'user.rate'


class Base(Entity):
    payload_generator = PayloadGenerator(ENTITY)

    def __init__(self, request):
        super().__init__(request)
        self.ttl = request.scope
        self.request = request
        self.payload_generator.request = request
        self.asserter = Asserter()

    def create(self, *args, **kwargs):
        pass

    def read(self, **data):
        api = self.urls['user']['rate']['read']
        url = api.format(protocol='https',
                         env=self.cmd_options['env'],
                         resource_id=data['resource_id'])
        response = self.rqst_session.get(url, cookies={
            'JSESSIONID': self.jsessionid})
        return response

    def update(self, **data):
        # Assign and Save the user new rate
        generated_id = self._assign(**data)
        data.update(generated_id=generated_id, delete_flag=False)
        response = self._save(**data)
        # verify the user rate update
        rates = self.verify_update(response, **data)
        data_str = {'resource_id': data['resource_id'], 'rates': rates}
        self.db_store.insert(self.scope, self.test_id, 'user', data_str)

    @payload_generator.generate_payload
    def _assign(self, **data):
        api = self.urls['user']['rate']['assign']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            resource_id=data['resource_id'])
        response = self.rqst_session.post(url, json=data['payload'],
                                          cookies={
                                              'JSESSIONID': self.jsessionid},
                                          )
        return response.json()['effectiveRates'][0]['id']

    @payload_generator.generate_payload
    def _save(self, **data):
        api = self.urls['user']['rate']['save']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            resource_id=data['resource_id'])
        response = self.rqst_session.post(url, json=data['payload'],
                                          cookies={
                                              'JSESSIONID': self.jsessionid},
                                          )
        return response

    @payload_generator.generate_payload
    def delete(self, **data):
        api = self.urls['user']['rate']['delete']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            resource_id=data['resource_id'])
        payload = data['payload']

        response = self.rqst_session.post(url, json=payload, cookies={
            'JSESSIONID': self.jsessionid})

    def verify_create(self, *args, **kwargs):
        pass

    def verify_update(self, response, **data):
        self.status = True
        self.step_desc = 'User rate update verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)

        ds = self.db_store.search_by_key('user', 'resource_id', data['resource_id'])
        if ds:
            rates = ds[0]['rates']
            if not rates:
                rates = []
        else:
            rates = []
        if response.status_code == 200:
            read_response = self.read(**data)
            if read_response.status_code == 200:
                actual_dct = read_response.json()
                expected_dct = data
                status = False
                for effectiverate in actual_dct['effectiveRates']:
                    # TODO: effective date verification
                    if effectiverate['rateId'] == int(
                            expected_dct['rate_id']):
                        user_rate_row_id = effectiverate['id']
                        effective_date = expected_dct['effective_date']

                        rate_id = effectiverate['rateId']
                        rates.append({'rate_id': rate_id,
                                      'generated_id': user_rate_row_id,
                                      'effective_date': effective_date})
                        status = True
                        self.remarks += 'User rate is updated'
                assert status
            else:
                self.status = False
                self.remarks += 'User rate updation failed \n failure traceback : {}'.format(
                    response.text)
        else:
            self.status = False
            self.remarks += response.text

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
        return rates

    def verify_delete(self, *args, **kwargs):
        pass
