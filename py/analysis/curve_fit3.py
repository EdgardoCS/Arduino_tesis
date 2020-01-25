"""
Steps:
1. Get Data from each subject and condition
2. Calculate mean
3. Adjust curve and plot
4. Calculate statistical difference based on curve/intercept
"""

import numpy as np
import pandas as pd
from scipy.misc import derivative
import sympy as sp

import sympy
from scipy.stats import stats
import matplotlib.pyplot as plt

# --- Get Data --- #
# set path

path = '../../data/parteII/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_exp3')
headers = dataFrame.columns
print(headers)

# establish initial conditions
trials = 6
min_subjects = 0
subjects = 3

speeds = [1, 3, 5, 10, 30, 50]  # six speeds


def def_plot(v1, v2):
    # plt.figure(a)

    # x_axis = np.array([1, 2, 3, 4, 5, 6])
    # xp = np.linspace(1, 6)

    x_axis = np.array([1, 2, 3, 4, 5, 6])
    xp = np.linspace(1, 6)
    y_axis = np.array(mean)

    z = np.polyfit(x_axis, y_axis, 2)
    p = np.poly1d(z)

    '''
    bounds = [3, 200]
    crit_points = bounds + [x for x in p.deriv().r if x.imag == 0 and bounds[0] < x.real < bounds[1]]
    print(crit_points)
    '''
    A = z[0]
    B = z[1]
    C = z[2]
    x_point = (-B) / (2 * A)

    print('max', x_point)

    # max_y = (A * (x_point ** 2)) + (B * x_point) + C  # Ax^2+Bx+C
    # print(x_point, max_y)
    # plt.plot(x_point, max_y, 'ro')
    plt.subplot(3, 1, a + 1)

    plt.title('Sujeto ' + str(a + 1))
    # plt.ylim(-10, 10)
    # plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.05, hspace=0.23)
    plt.plot(xp, p(xp), 'k-')


store_data, mean, sd, std = [], [], [], []
vas_column = 1
speed_column = 0

for a in range(min_subjects, subjects):
    mean = []
    for b in range(0, len(speeds)):
        print(speeds[b])
        for c in range(0, trials * len(speeds)):
            print(dataFrame)
            # print(dataFrame[headers[1]][c])
            # if dataFrame[headers[0]][c] == speeds[b]:
            #     store_data.append(dataFrame[headers[(a + vas_column)]][c])
            # if len(store_data) == trials:
            # # print(store_data)
            #     mean.append(np.mean(store_data))
            # store_data = []
            # # print(mean)
            # def_plot(mean, a)
