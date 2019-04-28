import numpy as np

from Machine_Learning.forward_pass import ForwardPass
from Machine_Learning.back_propogation import BackPropogation

np.set_printoptions(precision=2)


class TestClient:
    # def __init__(self):
    #     self.config = self.read_config_yml()
    #     self.input = self.set_input()
    #     self.wl1, self.wl2, self.alpha = self.set_weights_and_alpha()

    def __init__(self):
        self.input = np.array([[2,3]])

        # Layer 1 Weights that includes w1, w2, w3 and w4 from GD Program
        self.wl1 = np.array([[0.21, 0.13], [0.31, 0.10]])

        # Layer2 Weights that includes w5 and w6
        self.wl2 = np.array([[0.22], [0.23]])

        # Learning rate Alpha
        self.alpha = 0.05

    def read_config_yml(self):
        import yaml
        config = None
        with open("config_new.yml", 'r') as file:
            try:
                config = yaml.load(file)
            except yaml.YAMLError as exc:
                print(exc)
            finally:
                return config

    # def set_input(self):
    #     input1 = self.config['inputs']['value1']
    #     input2 = self.config['inputs']['value2']
    #     return np.array([[input1], [input2]])
    #
    # def set_weights_and_alpha(self):
    #     wl1, wl2 = self.construct_array(self.config)
    #     alpha = self.config['learning_rate']['alpha']
    #     return wl1, wl2, alpha

    # def construct_array(self, config):
    #     w_1234 = config['weights_layer_1']
    #     w_56 = config['weights_layer_2']
    #     w1 = w_1234['w1']
    #     w2 = w_1234['w2']
    #     w3 = w_1234['w3']
    #     w4 = w_1234['w4']
    #     w5 = w_56['w5']
    #     w6 = w_56['w6']
    #     wl1 = np.array([[w1, w2], [w3, w4]], dtype=float)
    #     wl2 = np.array([[w5], [w6]])
    #     return wl1, wl2

    def run_forward_pass(self):
        print('Performing Forward Pass')
        print('~' * 30)
        fp_obj = ForwardPass()
        self.a1 = fp_obj.compute_hidden_layers_for_h1_h2(self.input, self.wl1)
        print('Hidden layer - h', self.a1)
        output = fp_obj.compute_output_layer(self.wl2, self.a1)
        print('Inital output', output)

        initial_error, mean_err_square = fp_obj.compute_error(output)
        print('Initial Error>>>', initial_error)
        print('Mean Square error', mean_err_square)
        print('*' * 100)
        self.initial_error = initial_error
        return self

    def run_backward_propagation(self):
        error = self.initial_error
        print('Performing Backward Propagation')
        print('~' * 30)
        bp_obj = BackPropogation(self.alpha)
        self.final_wl1, self.final_wl2, self.final_error, self.final_output = bp_obj.perform_gradient_descent(
            self.input, self.wl1, self.wl2, error, self.a1)

        return self

    def run_backward_pass(self):
        error = self.initial_error
        print('Performing Backward Propagation')
        print('~' * 30)
        bp_obj = BackPropogation(self.alpha)
        self.final_wl1, self.final_wl2, self.final_error, self.final_output = bp_obj.perform_gradient_descent_for_one_iteration(self.input, self.wl1, self.wl2, error, self.a1)
        return self

    def display_output(self):
        print('Final Error', self.final_error)
        print('Final Output', self.final_output)
        print('Final w_1234', self.final_wl1)
        print('Final w_56', self.final_wl2)
        print('Total iteration taken for Gradient Descent', BackPropogation.iteration_count)


if __name__ == '__main__':
    TestClient().run_forward_pass().run_backward_pass().display_output()
