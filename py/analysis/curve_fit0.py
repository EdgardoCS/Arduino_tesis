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

path = '../../data/ParteI/data_sub-edited.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_available')
headers = dataFrame.columns
# read amount of columns with info
sub_index = len(pd.read_excel(path, header=0, sheet_name='trials_available').columns)

# establish initial conditions
trials = 5
fields = 6  # (vas,rnd) for each site
# subjects = int(sub_index / fields)
min_subjects = 0
subjects = 10

# set desired column in dataFrame (index)
exp0 = [0, 2, 4]
exp1 = [0, 2]
exp2 = [2, 4]

# exp = exp2
exp = exp1
speeds = [3, 10, 30, 50, 100, 200]  # six speeds


def def_plot(v1, v2, v3):
    # plt.figure(a)

    x_axis = np.array([3, 10, 30, 50, 100, 200])
    xp = np.linspace(3, 200)

    # x_axis = np.array([3, 10, 30, 50, 100, 200])
    # xp = np.linspace(3, 200)
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

    plt.subplot(2, 5, a + 1)

    plt.title('Sujeto ' + str(a + 1))
    # plt.ylim(-10, 10)
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.05, hspace=0.23)
    if d == 0:
        plt.plot(xp, p(xp), 'b')  # , label='Espalda (brush)')
    elif d == 2:
        plt.plot(xp, p(xp), 'g')  # , label='Antebrazo (brush)')
    elif d == 4:
        plt.plot(xp, p(xp), 'k.-', label='Antebrazo (tactor)')
    # legend = plt.legend(loc='upper right', fontsize='x-large')


store_data, mean, sd, std = [], [], [], []

for a in range(min_subjects, subjects):
    print('subject', a + 1)
    for d in exp:
        vas_column = d
        speed_column = d + 1
        print('experiment', d)
        mean = []
        for b in range(0, len(speeds)):
            for c in range(0, trials * len(speeds)):
                if dataFrame[headers[(a * fields + speed_column)]][c] == speeds[b]:
                    store_data.append(dataFrame[headers[(a * fields + vas_column)]][c])
                    if len(store_data) == trials:
                        # print(speeds[b])
                        # print(store_data)
                        mean.append(np.mean(store_data))
                        store_data = []
        # print(mean)
        def_plot(mean, d, a)
