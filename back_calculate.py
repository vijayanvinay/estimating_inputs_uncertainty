__author__ = 'vinay_vijayan'

from simulate_output import SimulateOutput

import numpy as np
import random

mean = [0, 0]
cov = [[1, 0], [0, 1]]
x_1 = 10
x_2 = 20
x_3 = 30
random.seed(200)
NUMBER_OF_SIMULATIONS = 100000
THRESHOLD = 0.005


if __name__ == '__main__':
    object_simulate = SimulateOutput()
    y_a, y_b = object_simulate.get_y_observed(x_1, x_2, x_3)

    list_good_vectors = []
    for i in range(0, NUMBER_OF_SIMULATIONS):
        epsilon_1, epsilon_2 = np.random.multivariate_normal(mean, cov).T
        x_1_mod = x_1 + epsilon_1
        x_2_mod = x_2 + epsilon_2
        y_1_simulated, y_2_simulated = SimulateOutput.get_estimated_y(x_1_mod, x_2_mod, x_3)

        if abs(y_1_simulated - y_a) < (THRESHOLD*y_a) and abs(y_2_simulated- y_b) < (THRESHOLD*y_b):
            list_good_vectors.append([x_1_mod, x_2_mod])

    x_1_actual, x_2_actual = object_simulate.get_x()

    x_1_estimated = np.mean([each[0] for each in list_good_vectors])
    x_2_estimated = np.mean([each[1] for each in list_good_vectors])

    print 'x_1_actual:'+' '+str(x_1_actual), 'x_1_estimated:'+' '+str(x_1_estimated)
    print 'x_2_actual:'+' '+str(x_2_actual), 'x_2_estimated:'+' '+str(x_2_estimated)

    pass
