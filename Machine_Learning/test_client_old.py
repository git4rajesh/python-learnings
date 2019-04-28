import numpy as np

from Machine_Learning.forward_pass import ForwardPass
from Machine_Learning.back_propogation import BackPropogation

# start_weights = np.array([[0.11, 0.12, 0.14], [0.21, 0.08, 0.15]], dtype=float)

# start_weights_1_2_3_4 = np.array([[0.11, 0.12], [0.21, 0.08]], dtype=float)
# start_weights_5_6 = np.array([[0.14], [0.15]])

np.set_printoptions(precision=2)

class TestClient:
    def __init__(self):
        self.input = np.array([[2], [3]])
        self.wl1, self.wl2 = self.construct_nd_array()
        # self.wl1, self.wl2 = self.set_weights()

    def construct_nd_array(self):
        weights = self.read_yml()
        w_1234 = weights['weights_layer_1']
        w_5_6 = weights['weights_layer_2']
        w1 = w_1234['w1']
        w2 = w_1234['w2']
        w3 = w_1234['w3']
        w4 = w_1234['w4']
        w5 = w_5_6['w5']
        w6 = w_5_6['w6']
        wl1 = np.array([[w1, w2], [w3, w4]], dtype=float)
        wl2 = np.array([[w5], [w6]])
        return wl1, wl2

    def read_yml(self):
        import yaml
        weights = None
        with open("weights.yml", 'r') as file:
            try:
                weights = yaml.load(file)
            except yaml.YAMLError as exc:
                print(exc)
            finally:
                return weights

    # def set_weights(self):
    #     w_1234 = start_weights_1_2_3_4
    #     w_5_6 = start_weights_5_6
    #     return w_1234, w_5_6

    # def set_weights_old(self):
    #     w_1234 = start_weights[:, 0:2]
    #     w_56 = np.array([start_weights[:, -1]]).transpose()
    #     return w_1234, w_56

    def run_forward_pass(self):
        fp_obj = ForwardPass()
        self.a1 = fp_obj.compute_hidden_layers_for_h1_h2(self.input, self.wl1)
        print('\na1', self.a1)
        output = fp_obj.compute_output_layer(self.wl2, self.a1)
        print('\nInital output', output)


        error, mean_err_square = fp_obj.compute_error(output)
        print('\nerror>>>', error)
        print('\mean sqr error', mean_err_square)
        return error

    def run_backward_propagation(self, error):
        bp_obj = BackPropogation()
        new_wl1, new_wl2, error, output = bp_obj.perform_gradient_descent(self.input, self.wl1, self.wl2, error, self.a1)
        print('Final Output>>> \n', output)
        print('\nFinal error\n', error)
        print('\nfinal set of wl1>>> \n', new_wl1)
        print('\nfinal set of wl2>>> \n', new_wl2)
        return new_wl1, new_wl2


if __name__ == '__main__':
    client = TestClient()
    error = client.run_forward_pass()
    client.run_backward_propagation(error)
