import os
import sys


path = os.path.join(os.path.dirname(__file__), '../../../../../..')
sys.path.extend([path])

from automation.fluent_ml.src import helper


# Card 1 start date and end date should be greater than Card 2 start date and end date
# Make sure the dates are atleast 2 days apart as the method returns only week days.
c1_planned_start, c1_planned_finish = helper.get_start_end_dates(4, 8)
c2_planned_start, c2_planned_finish = helper.get_start_end_dates(1, 5)

PVE_97504 = {'c1_planned_start': c1_planned_start, 'c1_planned_finish': c1_planned_finish,
    'c2_planned_start': c2_planned_start, 'c2_planned_finish': c2_planned_finish}

PVE_97560 = {'c1_planned_start': c1_planned_start, 'c1_planned_finish': c1_planned_finish,
    'c2_planned_start': c2_planned_start, 'c2_planned_finish': c2_planned_finish}

PVE_97561 = {'c1_planned_start': c1_planned_start, 'c1_planned_finish': c1_planned_finish}

# Data for test 97505
# Start date - C1> C2, End data - C2> C1
c1_planned_start, c1_planned_finish = helper.get_start_end_dates(4, 8)
c2_planned_start, c2_planned_finish = helper.get_start_end_dates(1, 11)
# Updated C2 Start date - C2>C1
updated_c2_planned_start, _ = helper.get_start_end_dates(7, 9)
# Updated End data - C1 > C2
_, updated_c1_planned_finish = helper.get_start_end_dates(10, 14)

PVE_97505 = {'c1_planned_start': c1_planned_start, 'c1_planned_finish': c1_planned_finish,
    'c2_planned_start': c2_planned_start, 'c2_planned_finish': c2_planned_finish,
    'updated_c2_planned_start': updated_c2_planned_start, 'updated_c1_planned_finish': updated_c1_planned_finish}


planned_start, planned_finish = helper.get_start_end_dates(4, 12)
scheduled_start, scheduled_finish = helper.get_prm_start_end_dates(1, 8)
PVE_97706 = {'name': 'Auto_Project_97706', 'scheduled_start': scheduled_start, 'scheduled_finish': scheduled_finish}

PVE_97712 = {'name': 'Auto_Project_97712', 'prm_scheduled_start': scheduled_start,
    'prm_scheduled_finish': scheduled_finish, 'lk_planned_start': planned_start, 'lk_planned_finish': planned_finish}

PVE_97710 = {'planned_start': planned_start, 'planned_finish': planned_finish}
