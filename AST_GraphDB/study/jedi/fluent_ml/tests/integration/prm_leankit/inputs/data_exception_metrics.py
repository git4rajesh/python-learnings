import os
import sys


path = os.path.join(os.path.dirname(__file__), '../../../../../..')
sys.path.extend([path])

from automation.fluent_ml.src import helper

# planned start and finish date less than current date
past_planned_start, past_planned_finish = helper.get_start_end_dates(-10, 5)
future_planned_start, future_planned_finish = helper.get_start_end_dates(10, 5)
start_and_finish_dates = {'past_start_date': past_planned_start,
    'past_finish_date': past_planned_finish, 'future_start_date': future_planned_start, 'future_finish_date': future_planned_finish}


planned_finish_parent, planned_finish_child = helper.get_start_end_dates(1, 8)

finish_dates = {'parent_finish_date': planned_finish_parent, 'child_finish_date': planned_finish_child}
