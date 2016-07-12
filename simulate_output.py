__author__ = 'vinay_vijayan'

import numpy as np
import math
import random

mean = [0, 0]
cov = [[1, 0], [0, 1]]
random.seed(300)


class SimulateOutput(object):
    def get_y_observed(self, x_1, x_2, x_3):

        epsilon_1, epsilon_2 = np.random.multivariate_normal(mean, cov).T
        self.x_1 = x_1 + epsilon_1
        self.x_2 = x_2 + epsilon_2
        self.x_3 = x_3

        y_1, y_2 = SimulateOutput.get_estimated_y(x_1, x_2, x_3)
        y_1 += np.random.normal(0, 5)
        y_2 += np.random.normal(0, 10)

        return y_1, y_2

    @staticmethod
    def get_estimated_y(x_1, x_2, x_3):
        y_1_estimated = x_1 + x_2 + x_3 + x_1 * x_2
        y_2_estimated = x_1 + math.pow(x_2, 4) + x_3 + x_1 * x_2
        return y_1_estimated, y_2_estimated

    def get_x(self):
        return self.x_1, self.x_2


if __name__ == '__main__':
    test_object = SimulateOutput()
    y_a, y_b = test_object.get_y(1, 2, 3)
    print(y_a, y_b)