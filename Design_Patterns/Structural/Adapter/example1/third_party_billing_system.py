class Third_Party_Billing_System:

    @staticmethod
    def process_salary(lst_emp_obj):
        for emp in lst_emp_obj:
            if emp.designation == 'Mgr':
                emp.salary = 1000
            elif emp.designation == 'QA':
                emp.salary = 2000

            elif emp.designation == 'Engr':
                emp.salary = 3000
            else:
                emp.salary = 5000

        return lst_emp_obj
