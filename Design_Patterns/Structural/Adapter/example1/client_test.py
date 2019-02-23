from Design_Patterns.Structural.Adapter.example1.emp_adapter import Emp_Adapter

from Design_Patterns.Structural.Adapter.example1.client_existing_hr_system import Existing_HR_System


class Client:
    def __init__(self):
        self.emp_adapter_obj = Emp_Adapter()

    def demo(self):
        existing_hr_system_obj = Existing_HR_System()
        lst_tup_emp = existing_hr_system_obj.emp_list_tup
        lst_emp_obj = self.emp_adapter_obj.process_company_salary(lst_tup_emp)

        for emp in lst_emp_obj:
            print(emp.name, emp.designation, emp.salary)
            print('\n')


if __name__ == '__main__':
    client = Client()
    client.demo()
