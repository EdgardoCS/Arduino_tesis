"""
Steps:
1. Get Data from each subject and condition
2. Calculate mean
3. Adjust curve and plot
4. Calculate statistical difference based on curve/intercept
"""

import numpy as np
import pandas as pd
from scipy.stats import stats
import matplotlib.pyplot as plt

# --- Get Data --- #
# set path

path = '../../data/parteI/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_available')
headers = dataFrame.columns
# read amount of columns with info
sub_index = len(pd.read_excel(path, header=0, sheet_name='trials_available').columns)

# establish initial conditions
trials = 5
fields = 6  # (vas,rnd) for each site
# subjects = int(sub_index / fields)
subjects = 15

# set desired column in dataFrame (index)
exp0 = [0, 2, 4]
exp1 = [0, 2]
exp2 = [2, 4]

# exp = exp2
exp = [4]
speeds = [3, 10, 30, 50, 100, 200]  # six speeds


def def_plot(v1, v2, v3):
    # plt.figure(a)

    x_axis = [1, 2, 3, 4, 5, 6]
    y_axis = np.array(mean)
    z1 = np.polyfit(x_axis, y_axis, 2)
    p1 = np.poly1d(z1)
    xp = np.linspace(1, 6)

    plt.subplot(3, 5, a + 1)
    plt.title('Sujeto ' + str(a + 1))
    plt.ylim(-10, 10)
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.05, hspace=0.23)
    if d == 0:
        plt.plot(xp, p1(xp), 'k-')  # , label='Espalda (brush)')
    elif d == 2:
        plt.plot(xp, p1(xp), 'k--')  # , label='Antebrazo (brush)')
    elif d == 4:
        plt.plot(xp, p1(xp), 'k.-', label='Antebrazo (tactor)')
    # legend = plt.legend(loc='upper right', fontsize='x-large')


store_data, mean, sd, std = [], [], [], []

for a in range(0, subjects):
    print('subject', a + 1)
    for d in exp:
        vas_column = d
        speed_column = d + 1
        print('experiment', d)
        mean = []
        for b in range(0, len(speeds)):
            for c in range(0, trials * fields):
                if dataFrame[headers[(a * fields + speed_column)]][c] == speeds[b]:
                    store_data.append(dataFrame[headers[(a * fields + vas_column)]][c])
                    if len(store_data) == trials:
                        mean.append(np.mean(store_data))
                        store_data = []
        print(mean)
        def_plot(mean, d, a)
