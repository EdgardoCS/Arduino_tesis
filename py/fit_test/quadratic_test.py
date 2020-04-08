"""
the following will calculate quadratic regression for each subject data at
site 1 (upper back) and plot altogether in the same plot

steps.
1. get data from each subject and condition
2. divide data in trial and test
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# set path
path = '../../stata/data.xlsx'
# read data form .xlsx file
dataFrame = pd.read_excel(path, header=1, sheet_name='data_etapa1(sorted)')  # training section
dataFrame2 = pd.read_excel(path, header=1, skiprows=18, sheet_name='data_etapa1(sorted)')  # testing section
headers = dataFrame.columns
headers2 = dataFrame2.columns

# read amount of subjects, based on quantity of columns with info
n_subjects = int((len(pd.read_excel(path, header=0, sheet_name='data_etapa1(sorted)').columns) - 1) / 3)
n_trials = 5

# set target test (1,2,3)
exp = 1
vel = 0  # speed will be always in column 0
speeds = [3, 10, 30, 50, 100, 200]


def test_fit(a, b, c, d, e):
    xp = np.linspace(3, 200)
    x_axis_train = np.array(storage_vel_train)
    y_axis_train = np.array(storage_vas_train)
    x_axis_test = np.array(storage_vel_test)
    y_axis_test = np.array(storage_vas_test)

    p1 = np.poly1d(np.polyfit(x_axis_train, y_axis_train, 1))
    p2 = np.poly1d(np.polyfit(x_axis_train, y_axis_train, 2))
    y1 = np.poly1d(np.polyfit(x_axis_test, y_axis_test, 1))
    y2 = np.poly1d(np.polyfit(x_axis_test, y_axis_test, 2))

    # plt.figure(e)
    # TRAINING DATA #
    plt.subplot(221)
    plt.scatter(x_axis_train, y_axis_train)
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Training Linear Regression')
    plt.plot(xp, p1(xp), c='r')
    r2_train = r2_score(y_axis_train, p1(x_axis_train))
    print('Linear train', 'The rsquared value is: ' + str(r2_train))

    plt.subplot(223)
    plt.scatter(x_axis_train, y_axis_train)
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Training Quadratic Regression')
    plt.plot(xp, p2(xp), c='r')
    r2_train2 = r2_score(y_axis_train, p2(x_axis_train))
    print('Quadratic train', 'The rsquared value is: ' + str(r2_train2))

    # TESTING DATA #
    plt.subplot(222)
    plt.scatter(x_axis_test, y_axis_test)
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Testing Linear Regression')
    plt.plot(xp, y1(xp), c='r')
    r2_test = r2_score(y_axis_test, y1(x_axis_test))
    print('Linear test', 'The rsquared value is: ' + str(r2_test))

    plt.subplot(224)
    plt.scatter(x_axis_test, y_axis_test)
    plt.xlabel('speed(mm/s^-1)')
    plt.ylabel('vas score')
    plt.title('Testing Quadratic Regression')
    plt.plot(xp, y2(xp), c='r')
    r2_test2 = r2_score(y_axis_test, y2(x_axis_test))
    print('Quadratic test', 'The rsquared value is: ' + str(r2_test2))


# read data and storage under two categories (trials, test)
# for a in range(0, n_subjects):
for a in range(0, 1):  # start with 1 subject for testing purpose
    subject = a + 1
    print('subject N°', subject)
    target_column = exp + (3 * a)
    storage_vas_train = []
    storage_vel_train = []
    storage_vas_test = []
    storage_vel_test = []
    for b in range(0, len(speeds)):  # this one moves across speeds
        for c in range(0, 18):  # this one moves vertically across column
            if dataFrame[headers[vel]][c] == speeds[b]:  # search for match
                storage_vas_train.append(int(dataFrame[headers[target_column]][c]))  # stores data from training target
                storage_vel_train.append(int(dataFrame[headers[vel]][c]))
        for d in range(0, 12):  # this one moves vertically across column
            if dataFrame2[headers2[vel]][d] == speeds[b]:  # search for match
                storage_vas_test.append(int(dataFrame2[headers2[target_column]][d]))  # stores data from testing target
                storage_vel_test.append(int(dataFrame2[headers2[vel]][d]))
    test_fit(storage_vas_train, storage_vel_train, storage_vas_test, storage_vel_test, subject)
