

def construct_subsection_lst(tsk_dict, sub_section_dct):
    temp_lst = []
    for task_id in tsk_dict.keys():
        sub_section_dct['taskNumber'] = tsk_dict[task_id]
        sub_section_dct['taskId'] = task_id
        temp_lst.append(sub_section_dct.copy())

    return temp_lst