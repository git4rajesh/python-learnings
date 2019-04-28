import numpy as np

# start_weights = np.array([[0.11, 0.12, 0.14], [0.21, 0.08, 0.15]], dtype=float)
np.set_printoptions(precision=2)


class ForwardPass:
    def __init__(self):
        pass

    def compute_hidden_layers_for_h1_h2(self, input, wl1):
        a1 = np.dot(input, wl1)
        # a1 = input.dot(wl1)
        return a1

    def compute_output_layer(self, wl2, a1):
        output = a1.dot(wl2)
        return output

    def compute_error(self, output):
        # Creating a ones matrix for actual output
        actual = np.ones(1)
        error = output - actual
        mean_err_square = self.compute_mean_error_square(error)
        return error, mean_err_square

    def compute_mean_error_square(self, error):
        mean_err_square = (0.5) * (error) * (error)
        return mean_err_square
