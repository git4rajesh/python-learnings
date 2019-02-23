class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

        self.salary = ''

    def get_emp_name(self):
        return self.name

    def get_emp_designation(self):
        return self.designation

    def set_emp_name(self, name):
        self.name = name

    def set_emp_designation(self, designation):
        self.designation = designation

    def get_emp_salary(self):
        return self.salary
