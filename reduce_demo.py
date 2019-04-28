from functools import reduce
from collections import OrderedDict

class reducedemo:

    def aggregate_hours(self, current_timesheet, next_timesheet):
        for date in current_timesheet:
            if date in next_timesheet:
                next_timesheet[date] += current_timesheet[date]
            else:
                next_timesheet[date] = current_timesheet[date]
        return next_timesheet


    # def aggregate_timesheets(self, verify_expected_dct):
    #     for category in verify_expected_dct:
    #         for week_start_date in verify_expected_dct[category]:
    #             verify_expected_dct[category][week_start_date] = reduce(self.aggregate_hours,
    #                                                                     verify_expected_dct[category][week_start_date])
    #     return verify_expected_dct


    def aggregate_timesheets(self, verify_expected_dct):
        self.verify_expected_dct = verify_expected_dct

        for category in verify_expected_dct:
            map(self.reduce_wrapper, verify_expected_dct[category].keys())


    def reduce_wrapper(self, week_start_date):
        for week_start_date in list_week_start_date:
            verify_expected_dct[category][week_timesheets] = reduce(self.aggregate_hours,
                                                                    self.verify_expected_dct[category][week_timesheets])
            return verify_expected_dct

if __name__ == '__main__':
    reduceobj = reducedemo()

    lst1 = OrderedDict([('2016-08-29T00:00:00.000Z', 1.0), ('2016-08-30T00:00:00.000Z', 1.0), ('2016-08-31T00:00:00.000Z', 6.0), ('2016-09-01T00:00:00.000Z', 6.0), ('2016-09-02T00:00:00.000Z', 6.0)])
    lst2 = OrderedDict([('2016-09-05T00:00:00.000Z', 1.0), ('2016-09-06T00:00:00.000Z', 2.0), ('2016-09-07T00:00:00.000Z', 6.0), ('2016-09-08T00:00:00.000Z', 1.0), ('2016-09-09T00:00:00.000Z', 2.0)])
    lst3 = OrderedDict([('2016-09-05T00:00:00.000Z', 6.0), ('2016-09-06T00:00:00.000Z', 1.0), ('2016-09-07T00:00:00.000Z', 1.0), ('2016-09-08T00:00:00.000Z', 1.0), ('2016-09-09T00:00:00.000Z', 6.0)])

    verify_expected_dct = {'UX': {'1': [lst1.copy()],
                                  '2': [lst2.copy(), lst3.copy()]
                                  }
                           }

    print(reduceobj.aggregate_timesheets(verify_expected_dct))