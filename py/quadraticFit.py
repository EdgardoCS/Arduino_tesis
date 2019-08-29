# the following script will plot a quadratic regression

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
plt.switch_backend('TkAgg')
# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')

# path = '../data/data_sub0.xlsx'
# dataFrame = pd.read_excel(path, header=2, sheet_name='trials_ex')

headers = dataFrame.columns

vas1 = []
vas2 = []
vas3 = []
vas4 = []
vas5 = []
vas6 = []

trials = 5
fields = 6
subjects = 9

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

meanData = []
speedData = []


# SORT DATA
def sortSecond(val):
    return val[1]


# color = ['g', 'r', 'c', 'm', 'y', 'b']
for y in range(0, 3):
    index_vas = y + y * 1  # neck(0); forearm(2); tactor(4);
    index_speed = index_vas + 1

    for t in range(0, subjects):
        for u in range(0, len(dataFrame)):
            # stores the VAS score from each subject in the neck area
            if dataFrame[headers[(t * fields + index_speed)]][u] == 3:
                vas1.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas1) == trials:
                    temp1.append(vas1)
                    meanData.append([np.mean(temp1), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas1 = []
            if dataFrame[headers[(t * fields) + index_speed]][u] == 10:
                vas2.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas2) == trials:
                    temp2.append(vas2)
                    meanData.append([np.mean(temp2), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas2 = []
            if dataFrame[headers[(t * fields) + index_speed]][u] == 30:
                vas3.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas3) == trials:
                    temp3.append(vas3)
                    meanData.append([np.mean(temp3), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas3 = []
            if dataFrame[headers[(t * fields) + index_speed]][u] == 50:
                vas4.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas4) == trials:
                    temp4.append(vas4)
                    meanData.append([np.mean(temp4), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas4 = []
            if dataFrame[headers[(t * fields) + index_speed]][u] == 100:
                vas5.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas5) == trials:
                    temp5.append(vas5)
                    meanData.append([np.mean(temp5), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas5 = []
            if dataFrame[headers[(t * fields) + index_speed]][u] == 200:
                vas6.append(dataFrame[headers[t * fields + index_vas]][u])
                if len(vas6) == trials:
                    temp6.append(vas6)
                    meanData.append([np.mean(temp6), dataFrame[headers[(t * fields + index_speed)]][u]])
                    vas6 = []

        # print(meanData)
        meanData.sort(key=sortSecond)
        for i in range(0, len(meanData)):
            speedData.append(meanData[i].pop())

        new_x = np.array(speedData).reshape(-1, 1)
        new_y = np.concatenate(meanData)

        # print(new_x)
        # print(new_y)

        lin = LinearRegression()
        lin.fit(new_x, new_y)

        poly = PolynomialFeatures(degree=5)
        x_poly = poly.fit_transform(new_x)

        poly.fit(x_poly, new_y)
        lin2 = LinearRegression()
        lin2.fit(x_poly, new_y)

        fig1 = plt.figure(y)

        # plt.scatter(new_x, new_y, color='b')
        # plt.plot(new_x, lin.predict(new_x), color='r')
        # plt.title('Linear Regression')
        # plt.xscale('log')
        # plt.xlabel('Speed')
        # plt.ylabel('VAS score')

        # plt.scatter(new_x, new_y, color='k')
        plt.plot(new_x, lin2.predict(poly.fit_transform(new_x)), color='b')
        plt.title('Polynomial Regression')
        # plt.yticks((-10, -7, -5, -3, -1, 0, 1, 3, 5, 7, 10))
        plt.xscale('log')
        plt.xlabel('Speed')
        plt.ylabel('VAS score')

        meanData = []
        speedData = []

        fig1.show()
