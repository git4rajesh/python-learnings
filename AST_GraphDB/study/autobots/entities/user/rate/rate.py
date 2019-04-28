import datetime

from entities.user.rate.base import Base

ENTITY = 'user.rate'


class Rate(Base):
    def __init__(self, request):
        super().__init__(request)
        self.rate_table = {}

    def set_rate(self, rate, resource_id, days_offset=1):
        """
        set internal rate
        :param rate:
        :param resource_id:
        :param days_offset:
        :return:
        """
        # Check for effective date else create default date
        today = datetime.date.today()
        prev_monday = today - datetime.timedelta(days=today.weekday(), weeks=1)
        effective_date = prev_monday + datetime.timedelta(days=days_offset-1)
        effective_date_frmt = effective_date.strftime('%Y-%m-%dT01:01:01')

        # Assign the internal rate
        data = {'resource_id': resource_id, 'effective_date': effective_date_frmt,
                'rate_id': self.constants['RATES'][rate]['ID'],
                'generated_id': 0}
        super().update(**data)

    def _get_rate_table(self, user):
        resource_id = self.request.config.option.users[user]['resource_id']
        data = {'resource_id': resource_id}
        rate_det = super().read(**data)
        effective_rates = rate_det.json()['effectiveRates']
        self.rate_table.update({user: effective_rates})
        return self.rate_table

    def get_rate(self, user, date_str):
        """
        Get rate for the given user and for the date
        :param user: user name
        :param date_str: date in format yyyy-mm-ddT00:00:00:000+0000
        :return: returns the opExRate from the rate table
        """
        rate_date = self._str_to_date(date_str)
        effective_rates = self.rate_table.get(user)
        if not effective_rates:
            rate_table = self._get_rate_table(user)
            effective_rates = rate_table.get(user)

        for effective_rate in effective_rates:
            from_date = self._str_to_date(effective_rate['fromDate'])
            to_date = self._str_to_date(effective_rate['toDate'])
            if ((from_date == 'past' or from_date <= rate_date) and
                    (to_date == 'future' or rate_date <= to_date)):
                for rate in effective_rate['rateTable']:
                    rate_frm_date = self._str_to_date(rate['fromDate'])
                    rate_to_date = self._str_to_date(rate['toDate'])
                    if ((rate_frm_date == 'past' or rate_frm_date <= rate_date) and
                            (rate_to_date == 'future' or rate_date <= rate_to_date)):
                        return float(rate['opExRate'])

    def _str_to_date(self, date_str):
        if date_str.lower() == 'future' or date_str.lower() == 'past':
            return date_str.lower()
        date_frmt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_frmt
