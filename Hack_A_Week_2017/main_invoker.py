from Hack_A_Week.testcase_generator import TestCaseGen


class MainInvoker:
    def run(self, n_wise):
        tc_gen_obj = TestCaseGen(n_wise)
        tc_gen_obj.distribute_field_values()


if __name__ == '__main__':
    main_obj = MainInvoker()
    main_obj.run(2)
