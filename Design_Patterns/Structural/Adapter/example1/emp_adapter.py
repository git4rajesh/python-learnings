from Design_Patterns.Structural.Adapter.example1.third_party_billing_system import Third_Party_Billing_System

from Design_Patterns.Structural.Adapter.example1.employee import Employee


class Emp_Adapter:

    def process_company_salary(self, lst_tup_emp):
        lst_emp_obj = self.construct_emp_lst(lst_tup_emp)
        return Third_Party_Billing_System.process_salary(lst_emp_obj)

    def construct_emp_lst(self, lst_tup_emp):
        lst_emp_obj = []
        for item in lst_tup_emp:
            emp_obj = Employee(item[0], item[1])
            lst_emp_obj.append(emp_obj)

        return lst_emp_obj
