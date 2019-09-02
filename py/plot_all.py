# the following script will plot the maximun value for each trial
# every subject has 5 trials


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mean1 = []
mean2 = []
mean3 = []
mean4 = []
mean5 = []
mean6 = []


## functions ##
def plot_data(max1, max2, max3, max4, max5, max6):
    bars = ('3', '10', '30', '50', '100', '200')
    y_pos = np.arange(len(bars))
    y = [len(mean1), len(mean2), len(mean3), len(mean4), len(mean5), len(mean6)]
    plt.figure(0)
    #plt.scatter(y_pos, y, color='k')
    plt.bar(y_pos, y, width=0.6)
    plt.xticks(y_pos, bars)
    plt.title('Subjects')


# GET DATA
# read data from xlsx
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')
headers = dataFrame.columns

# initial conditions
subjects = 10  # number of subjects
trials = 5  # number of trials
speeds = 6  # six speed were tested (3, 10 , 30 , 50 , 100, 200)

# variables
data = []  # stores raw data
vel = []  # stores each speed
'''
max1 = []  # stores maximum value for given dataset(trial)
max2 = []
max3 = []
max4 = []
max5 = []
max6 = []
'''
for s in range(0, subjects):
    # stores maximum value for given dataset(trial)
    max1 = None
    max2 = None
    max3 = None
    max4 = None
    max5 = None
    max6 = None
    for t in range(0, (trials * speeds)):

        # for loop through all data for each s
        # subject
        # 30 values = VAS score
        condition1 = (s * 6)
        condition2 = (s * 6) + 2
        condition3 = (s * 6) + 4

        condition = condition3

        data.append(dataFrame[headers[condition]][t])  # headers[0] equals to score
        vel.append(dataFrame[headers[condition + 1]][t])  # headers[1] equals to score
        if len(data) == speeds:  # times speeds were tested
            pos = np.argmax(data)
            # condition to add data to each max
            if vel[pos] == 3:
                max1 = np.amax(data)
                mean1.append(max1)
            if vel[pos] == 10:
                max2 = np.amax(data)
                mean2.append(max2)
            if vel[pos] == 30:
                max3 = np.amax(data)
                mean3.append(max3)
            if vel[pos] == 50:
                max4 = np.amax(data)
                mean4.append(max4)
            if vel[pos] == 100:
                max5 = np.amax(data)
                mean5.append(max5)
            if vel[pos] == 200:
                max6 = np.amax(data)
                mean6.append(max6)
            data = []
            vel = []
plot_data(max1, max2, max3, max4, max5, max6)
