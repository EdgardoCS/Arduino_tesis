# the following script will plot a quadratic regression


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

## GET DATA
path = '../data/data_sub.xlsx'

dataFrame = pd.read_excel(path, header=2, sheet_name='trials_ex')
headers = dataFrame.columns

vasSubjectNeck1 = []
vasSubjectNeck2 = []
vasSubjectNeck3 = []
vasSubjectNeck4 = []
vasSubjectNeck5 = []
vasSubjectNeck6 = []

trials = 5
fields = 6
subjects = 5

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

meanData = []
speedData = []

index_vas = 0  # neck(0); forearm(2); tactor(4);
index_speed = index_vas + 1


## SORT DATA
def sortSecond(val):
    return val[1]


for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + index_speed)]][u] == 3:
            vasSubjectNeck1.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck1) == trials:
                temp1.append(vasSubjectNeck1)
                meanData.append([np.mean(temp1), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck1 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 10:
            vasSubjectNeck2.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck2) == trials:
                temp2.append(vasSubjectNeck2)
                meanData.append([np.mean(temp2), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck2 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 30:
            vasSubjectNeck3.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck3) == trials:
                temp3.append(vasSubjectNeck3)
                meanData.append([np.mean(temp3), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck3 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 50:
            vasSubjectNeck4.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck4) == trials:
                temp4.append(vasSubjectNeck4)
                meanData.append([np.mean(temp4), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck4 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 100:
            vasSubjectNeck5.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck5) == trials:
                temp5.append(vasSubjectNeck5)
                meanData.append([np.mean(temp5), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck5 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 200:
            vasSubjectNeck6.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck6) == trials:
                temp6.append(vasSubjectNeck6)
                meanData.append([np.mean(temp6), dataFrame[headers[(t * fields + index_speed)]][u]])
                vasSubjectNeck6 = []

    meanData.sort(key=sortSecond)
    for i in range(0, len(meanData)):
        speedData.append(meanData[i].pop())

    new_x = np.array(speedData).reshape(-1, 1)
    new_y = np.concatenate(meanData)

    print(new_x)
    print(new_y)

    lin = LinearRegression()
    lin.fit(new_x, new_y)

    poly = PolynomialFeatures(degree=5)
    x_poly = poly.fit_transform(new_x)

    poly.fit(x_poly, new_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, new_y)

    # plt.scatter(new_x, new_y, color='b')
    # plt.plot(new_x, lin.predict(new_x), color='r')
    # plt.title('Linear Regression')
    # plt.yticks((-10, -5, 0, 5, 10))
    # plt.xlabel('Speed')
    # plt.ylabel('VAS score')
    # plt.show()

    plt.scatter(new_x, new_y, color='b')
    plt.plot(new_x, lin2.predict(poly.fit_transform(new_x)), color='r')
    plt.title('Polynomial Regression')
    plt.yticks((-10, -5, -1, 0, 1, 5, 10))
    plt.xscale('log')
    plt.xlabel('Speed')
    plt.ylabel('VAS score')
    plt.show()

    meanData = []
    speedData = []
# # plt.scatter(new_x, new_y, color='b')
# # plt.plot(new_x, lin.predict(new_x), color='r')
# # plt.xscale('log')
# # plt.title('Linear Regression')
# # plt.xlabel('Speed')
# # plt.ylabel('VAS score')
# # plt.show()
# #
# # plt.scatter(new_x, new_y, color='b')
# # plt.xscale('log')
# # plt.plot(new_x, lin2.predict(poly.fit_transform(new_x)), color='r')
# # plt.xscale('log')
# # plt.title('Polynomial Regression log')
# # plt.xlabel('Speed')
# # plt.ylabel('VAS score')
#
plt.show()
