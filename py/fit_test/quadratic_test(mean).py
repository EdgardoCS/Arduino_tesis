"""
the following will calculate linear and quadratic regression for each subject data (median) at
site 1 (upper back) and plot altogether in the same plot
objective: determine which regression is the best fit for (n=15) subject's data

steps.
1. get data from each subject and condition
2. divide data in trial and test
3. calculate linear regression
4. calculate quadratic regression
5. calculate rsquare
6. next subject
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# set path
path = '../../stata/data.xlsx'
# read data form .xlsx file
dataFrame = pd.read_excel(path, header=1, sheet_name='data_etapa1_media')  # training section
headers = dataFrame.columns

# read amount of subjects, based on quantity of columns with info
n_subjects = int((len(pd.read_excel(path, header=0, sheet_name='data_etapa1_media').columns) - 1) / 3)
n_trials = 5

# set target test (1,2,3)
exp = 1
vel = 0  # speed will be always in column 0
speeds = [3, 10, 30, 50, 100, 200]


def test_fit(a, b, e):
    xp = np.linspace(3, 200, 25)
    y_axis = np.array(a)
    x_axis = np.array(b)

    p1 = np.poly1d(np.polyfit(x_axis, y_axis, 1))
    p2 = np.poly1d(np.polyfit(x_axis, y_axis, 2))

    plt.figure(e, figsize=(4, 6))
    plt.subplots_adjust(left=None, bottom=0.09, right=None, top=0.95, wspace=None, hspace=0.35)
    # TRAINING DATA #
    plt.subplot(211)
    plt.scatter(x_axis, y_axis, color='b')
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Linear Regression')
    plt.plot(xp, p1(xp), c='r')
    r2_train = r2_score(y_axis, p1(x_axis))
    print('Linear', 'The r_squared value is: ' + str(r2_train))

    plt.subplot(212)
    plt.scatter(x_axis, y_axis, color='b')
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Quadratic Regression')
    plt.plot(xp, p2(xp), c='r')
    r2_train2 = r2_score(y_axis, p2(x_axis))
    print('Quadratic', 'The r_squared value is: ' + str(r2_train2))


# read data and storage under two categories (trials, test)
for a in range(0, n_subjects):
    # for a in range(0, 1):  # start with 1 subject for testing purpose
    subject = a + 1
    print('subject N°', subject)
    target_column = exp + (3 * a)
    storage_vas = []
    storage_vel = []
    for b in range(0, len(speeds)):  # this one moves across speeds
        for c in range(0, 6):  # this one moves vertically across column
            if dataFrame[headers[vel]][c] == speeds[b]:  # search for match
                storage_vas.append(dataFrame[headers[target_column]][c])  # stores data from training target
                storage_vel.append(dataFrame[headers[vel]][c])
    # print(storage_vas)
    # print(storage_vel)
    test_fit(storage_vas, storage_vel, subject)
