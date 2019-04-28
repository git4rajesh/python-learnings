import json
from xlrd import open_workbook
from collections import OrderedDict


class ConstantJSONGenerator:
    DICT_OF_TESTS = OrderedDict()

    def __read_excel(self):
        workbook = open_workbook(self.excel_file)
        sheets = workbook.sheet_names()
        work_sheet = workbook.sheet_by_name(sheets[0])
        num_rows = work_sheet.nrows
        num_cols = work_sheet.ncols
        header = [work_sheet.cell_value(0, cell) for cell in range(num_cols)]
        for row_idx in range(1, num_rows):
            row_cell = [work_sheet.cell_value(row_idx, col_idx) for col_idx in range(num_cols)]
            ConstantJSONGenerator.__is_float_convert_int(row_cell)
            yield dict(zip(header, row_cell))

    @staticmethod
    def __is_float_convert_int(row_cell):
        for (index, float_num) in enumerate(row_cell):
            if isinstance(float_num, float):
                row_cell[index] = int(row_cell[index])

    def construct_master_dict(self):
        count = 0
        for row in self.__read_excel():
            count += 1
            dict_key = self.report_name + '_' + str(count)
            ConstantJSONGenerator.DICT_OF_TESTS[dict_key] = row

    @staticmethod
    def convert_dict_to_json():
        return json.dumps(ConstantJSONGenerator.DICT_OF_TESTS)

    def __get_input_from_user(self):
        self.env_name = input('Env Name:(POC41)\n') or 'POC41'
        self.db_name = input('DB Name: (PVE)\n') or 'PVE'
        self.user_name = input('User Name:(jharris)\n') or 'jharris'
        self.excel_file = input('Excel file:(wrk14_output.xlsx)\n') or 'wrk14_output.xlsx'
        self.report_name = input('Report Name:(RPM_WRK14_PR)\n') or 'RPM_WRK14_PR'
        self.structure_code = input('Structure Code:(1892)\n') or '1892'
        self.owner_type = input('Owner Type:($User)\n') or '$User'
        self.report_key = input('Report Key: (work_rpm_wrk14_pr)\n') or 'work_rpm_wrk14_pr'

    def __init__(self):
        self.env_name = ''
        self.report_name = ''
        self.db_name = ''
        self.user_name = ''
        self.structure_code = ''
        self.owner_type = ''
        self.report_key = ''
        self.json_dumps = ''
        self.__get_input_from_user()


if __name__ == '__main__':
    cgc_object = ConstantJSONGenerator()
    cgc_object.construct_master_dict()
    cgc_object.json_dumps = cgc_object.convert_dict_to_json()
    print(cgc_object.json_dumps)