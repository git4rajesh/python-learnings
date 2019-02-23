from Design_Patterns.Structural.Adapter.example2.TargetDictClass import TargetDict


class DictAdapter:
    def __init__(self):
        pass

    def show_dict_wrapper(self, source_arr_obj):
        two_dim_arr = source_arr_obj.my_array
        my_dct = dict(two_dim_arr)
        target_obj = TargetDict()
        target_obj.show_dict(my_dct)
