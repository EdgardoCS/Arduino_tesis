# the following script will plot a quadratic regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.switch_backend('TkAgg')
# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')
headers = dataFrame.columns

subjects = 9
sites = 1
speedData = []


# SORT DATA
def sortSecond(val):
    return val[1]


def get_data(dataFrame, headers, subjects, indexVas, indexSpeed):
    # set initial conditions
    trials = 5
    fields = 6

    vas3 = []
    vas10 = []
    vas30 = []
    vas50 = []
    vas100 = []
    vas200 = []
    # first we have to obtain the data from the dataFrame
    # each subject has the data pair (vasScore, stimulationSpeed)
    for s in range(0, subjects):
        for t in range(0, trials * 6):
            # store the vas score from each subject in the target site
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 3:
                vas3.append(dataFrame[headers[s * fields + indexVas]][t])
                # once the score is collected, its necessary to calculate the mean for each subject
                if len(vas3) == trials:
                    sdData.append([np.std(vas3), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas3), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas3 = []  # empty variable
            # then the process is repeated for each speed
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 10:
                vas10.append(dataFrame[headers[s * fields + indexVas]][t])
                if len(vas10) == trials:
                    sdData.append([np.std(vas10), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas10), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas10 = []
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 30:
                vas30.append(dataFrame[headers[s * fields + indexVas]][t])
                if len(vas30) == trials:
                    sdData.append([np.std(vas30), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas30), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas30 = []
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 50:
                vas50.append(dataFrame[headers[s * fields + indexVas]][t])
                if len(vas50) == trials:
                    sdData.append([np.std(vas50), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas50), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas50 = []
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 100:
                vas100.append(dataFrame[headers[s * fields + indexVas]][t])
                if len(vas100) == trials:
                    sdData.append([np.std(vas100), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas100), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas100 = []
            if dataFrame[headers[(s * fields + indexSpeed)]][t] == 200:
                vas200.append(dataFrame[headers[s * fields + indexVas]][t])
                if len(vas200) == trials:
                    sdData.append([np.std(vas200), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    meanData.append([np.mean(vas200), dataFrame[headers[(s * fields + indexSpeed)]][t]])
                    vas200 = []
    meanData.sort(key=sortSecond)
    sdData.sort(key=sortSecond)
    return meanData, sdData


def plot_data(new_x, new_y, u):
    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(new_x)

    poly.fit(x_poly, new_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, new_y)

    fig1 = plt.figure(u)

    plt.scatter(new_x, new_y, color='k')
    plt.plot(new_x, lin2.predict(poly.fit_transform(new_x)), color='b')
    plt.title('Polynomial Regression')
    # plt.yticks((-10, -7, -5, -3, -1, 0, 1, 3, 5, 7, 10))
    plt.xscale('log')
    plt.xlabel('Speed')
    plt.ylabel('VAS score')
    fig1.show()


for u in range(0, sites):
    # set initial conditions
    sdData = []
    meanData = []
    speedData = []

    # indexVas moves across the data
    # in data_sub.xlsx -- 0 for neck, 2 for forearm(brush), and 4 for forearm(tactor)
    indexVas = u + u * 1
    indexSpeed = indexVas + 1

    get_data(dataFrame, headers, subjects, indexVas, indexSpeed)

    # prepare data to plot
    for i in range(0, len(meanData)):
        speedData.append(meanData[i].pop())
    new_x = np.array(speedData).reshape(-1, 1)
    new_y = np.concatenate(meanData)
    # plot data each time
    plot_data(new_x, new_y, u)
