import numpy as np

from Machine_Learning.forward_pass import ForwardPass


class BackPropogation:
    iteration_count = 0
    def __init__(self, alpha):
        self.alpha = alpha

    def compute_new_wl1(self, wl1, alpha, error, input, wl2):
        """ Weights for layer1 computed which includes w1, w2, w3 and w4"""
        second_term = (alpha * error * input * wl2).transpose()
        new_wl1 = wl1 - second_term
        return new_wl1

    def compute_new_wl2(self, wl2, alpha, error, a1):
        second_term = (alpha * error * a1).transpose()
        new_wl2 = wl2 - second_term
        return new_wl2

    def perform_gradient_descent_for_one_iteration(self, input, wl1, wl2, actual_error, a1):
        fp = ForwardPass()
        actual_error = actual_error.astype(np.float16)[0][0]

        new_wl1 = self.compute_new_wl1(wl1, self.alpha, actual_error, input, wl2)
        new_wl2 = self.compute_new_wl2(wl2, self.alpha, actual_error, a1)
        a1 = fp.compute_hidden_layers_for_h1_h2(input, new_wl1)
        output = fp.compute_output_layer(new_wl2, a1)
        error, mean_error_square = fp.compute_error(output)

        return new_wl1, new_wl2, error, output

    def perform_gradient_descent(self, input, wl1, wl2, actual_error, a1):
        BackPropogation.iteration_count += 1
        fp = ForwardPass()
        actual_error = actual_error.astype(np.float16)[0][0]
        act_err = round(actual_error, 2)

        expected_error = np.zeros(shape=(1,1)).astype(np.float16)[0][0]

        new_wl1 = self.compute_new_wl1(wl1, self.alpha, actual_error, input, wl2)
        new_wl2 = self.compute_new_wl2(wl2, self.alpha, actual_error, a1)
        a1 = fp.compute_hidden_layers_for_h1_h2(input, new_wl1)
        output = fp.compute_output_layer(new_wl2, a1)
        error, mean_error_square = fp.compute_error(output)
        if act_err < expected_error:
            return self.perform_gradient_descent(input, new_wl1, new_wl2, error, a1)
        else:
            return new_wl1, new_wl2, error, output

