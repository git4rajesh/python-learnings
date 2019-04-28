class SideEffects:

    def __init__(self):
        self.var = 5

    def cause_side_effect(self):
        self.var = (5 * self.var) - 2

    def mitigate_side_effect(self):
        temp_var = 0
        temp_var = 5 * self.var - 2
        return temp_var

    def main_impact_seen(self):
        print(self.var)

if __name__ == '__main__':
    obj = SideEffects();
    obj.main_impact_seen()
    print(obj.cause_side_effect())
    obj.main_impact_seen()

    # obj.main_impact_seen()
    # print(obj.mitigate_side_effect())
    # obj.main_impact_seen()