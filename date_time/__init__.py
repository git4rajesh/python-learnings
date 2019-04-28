import numpy as np
from datetime import datetime

# start = dt.date( 2017, 5, 2 )
# end = dt.date( 2017, 5, 10 )

# days = np.busday_count( start, end )
#
# print('>>>', days)


from workdays import networkdays


str_start_date = '2013-07-29'
str_end_date = '2013-08-19'

start = datetime.strptime(str_start_date, '%Y-%m-%d').date()
end = datetime.strptime(str_end_date, '%Y-%m-%d').date()
days = networkdays(start,end)
print('>>>', days)