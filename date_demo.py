import time

class DateDemo:

    @staticmethod
    def is_date_compare(date1, date2):
        if date1 == date2:
            return 0
        elif date1 > date2:
            return 1
        else:
            return -1


    def convert_str_date(self):
        date1 = time.strptime('2016-09-09', '%Y-%m-%d')
        date2 = time.strptime('2016-09-08', '%Y-%m-%d')
        date3 = time.strptime('2016-09-10', '%Y-%m-%d')

        print(self.is_date_compare(date1, date2))
        print(self.is_date_compare(date1, date3))
        print(self.is_date_compare(date1, date1))

if __name__ == '__main__':
    d = DateDemo()
    d.convert_str_date()