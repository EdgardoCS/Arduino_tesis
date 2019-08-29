import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')

trials = 5
fields = 6
subjects = 9

meanData = []
sdData = []
speedData = []


# SORT DATA
def sortSecond(val):
    return val[1]


# color = ['g', 'r', 'c', 'm', 'y', 'b']
# for y in range(0, 3):
#     index_vas = y + y * 1  # neck(0); forearm(2); tactor(4);
#     index_speed = index_vas + 1
index_vas = 0
index_speed = 1

# for t in range(0, subjects):
t = 0

headers = dataFrame.columns
    # set initial variables empty
vas1 = []
vas2 = []
vas3 = []
vas4 = []
vas5 = []
vas6 = []

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
    # function to obtain data from dataFrame

t = 0
for u in range(0, len(dataFrame)):
    # stores the VAS score from each subject in the neck area
    if dataFrame[headers[(t * fields + index_speed)]][u] == 3:
        vas1.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas1) == trials:
            temp1.append(vas1)
            sdData.append([np.std(temp1), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp1), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas1 = []
    if dataFrame[headers[(t * fields) + index_speed]][u] == 10:
        vas2.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas2) == trials:
            temp2.append(vas2)
            sdData.append([np.std(temp2), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp2), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas2 = []
    if dataFrame[headers[(t * fields) + index_speed]][u] == 30:
        vas3.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas3) == trials:
            temp3.append(vas3)
            sdData.append([np.std(temp3), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp3), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas3 = []
    if dataFrame[headers[(t * fields) + index_speed]][u] == 50:
        vas4.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas4) == trials:
            temp4.append(vas4)
            sdData.append([np.std(temp4), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp4), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas4 = []
    if dataFrame[headers[(t * fields) + index_speed]][u] == 100:
        vas5.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas5) == trials:
            temp5.append(vas5)
            sdData.append([np.std(temp5), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp5), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas5 = []
    if dataFrame[headers[(t * fields) + index_speed]][u] == 200:
        vas6.append(dataFrame[headers[t * fields + index_vas]][u])
        if len(vas6) == trials:
            temp6.append(vas6)
            sdData.append([np.std(temp6), dataFrame[headers[(t * fields + index_speed)]][u]])
            meanData.append([np.mean(temp6), dataFrame[headers[(t * fields + index_speed)]][u]])
            vas6 = []

# print(meanData)
meanData.sort(key=sortSecond)
sdData.sort(key=sortSecond)


# print(meanData)
# print(sdData)

for i in range(0, len(meanData)):
    del (meanData[i][1])
    del (sdData[i][1])

n = 6
labels = ['3', '10', '30', '50', '100', '200']
x = np.arange(len(labels))
width = 0.35

mean = np.concatenate(meanData)
std = np.concatenate(sdData)
ind = np.arange(n)
plt.bar(ind, mean, width, yerr=std)
plt.show()

print(meanData)
print(sdData)
