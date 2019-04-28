from bs4 import BeautifulSoup


def get_all_leaf_tasks(data_store, parent_id):
    lst_leaf_tasks = _get_leaf_tasks(data_store, parent_id, [])
    return lst_leaf_tasks


def _get_leaf_tasks(data_store, parent_id, lst_leaf_tasks):
    leaf_tasks = data_store.search_by_key('task', 'parentId.value', parent_id)
    if leaf_tasks:
        lst_leaf_tasks += leaf_tasks
        for leaf_task in leaf_tasks:
            lst_leaf_tasks = _get_leaf_tasks(data_store, leaf_task['id'], lst_leaf_tasks)
    return lst_leaf_tasks


def parse_to_dict(html):
    time_row_keys = ['Billable Hrs', 'Non Billable Hrs', 'Total Hours', 'Billable Cost', 'Non Billable Cost',
                     'Capitalized Cost',
                     'Non-Capitalized Cost', 'Total Cost', 'Revenue', 'Non Billable Amount', 'Profit',
                     'Margin']
    time_column_keys = ['time', 'estimated', 'actual', 'variance', '% recognized']

    soup = BeautifulSoup(html, 'html5lib')
    rollup_dict = {}
    table = soup.find('table', {'class': 'dashBoardTable'})
    table_rows_lst = table.find_all('tr')
    for index, table_row in enumerate(table_rows_lst[:13]):
        row_data_lst = table_row.find_all('td')
        if index == 0:
            for heading_index, column_heading in enumerate(row_data_lst):
                column_heading = column_heading.text
                if time_column_keys[heading_index].lower() != column_heading.lower():
                    raise Exception(
                        'HTML Parse Error : Expected Heading : {0} and Actual Heading : {1}'.format(
                            time_column_keys[heading_index],
                            column_heading))
        else:
            rollup_inner_dct = {}
            for data_index, data in enumerate(row_data_lst):
                data_txt = data.text
                if data_index == 0 and time_row_keys[index - 1].lower() != data_txt.lower():
                    raise Exception(
                        'HTML Parse Error : Expected Row Key : {0} and Actual Row Key : {1}'.format(
                            time_row_keys[index - 1],
                            data_txt))
                elif data_index != 0:
                    if '(' in data_txt and ')' in data_txt:
                        data_txt = data_txt.replace('(', '-').replace(')', '')
                    data_formatted = float(data_txt.replace('Rs', '').replace('$', '').replace(',', '').replace(
                        ' ', '').replace('%', ''))
                    rollup_inner_dct[time_column_keys[data_index]] = data_formatted

            rollup_dict[time_row_keys[index - 1]] = rollup_inner_dct

    return rollup_dict
