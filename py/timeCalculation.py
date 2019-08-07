# calculation of time (in seconds) that elapsed between the stimulation is applied and the VAS
# score is register

import time
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import timedelta
import matplotlib.pyplot as plt

# set path
path = '../data/data_sub.xlsx'

dataFrame = pd.read_excel(path, header=(2), sheet_name='trials_ex')
headers = dataFrame.columns

vasSubjectNeck = []
vasSubjectForearm = []
vasSubjectTactor = []
vasResult1 = []
vasResult2 = []
vasResult3 = []

vas1 = []
vas2 = []
vas3 = []

speed1 = []
speed2 = []
speed3 = []

fields = 11
subjects = 3

# print(dataFrame[headers[2]])
for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        vasResult1.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 2]][u]])
    vasSubjectNeck.append(vasResult1)
    for u in range(0, len(dataFrame)):
        vasResult2.append([dataFrame[headers[(t * fields) + 4]][u], dataFrame[headers[(t * fields) + 6]][u]])
    vasSubjectForearm.append(vasResult2)
    for u in range(0, len(dataFrame)):
        vasResult3.append([dataFrame[headers[(t * fields) + 8]][u], dataFrame[headers[(t * fields) + 10]][u]])
    vasSubjectTactor.append(vasResult3)

# print(vasSubjectNeck)
# print(vasSubjectForearm)
# print(vasSubjectTactor)

for a in range(0, subjects):
    for b in range(0, len(vasSubjectNeck[a])):
        # NECK
        if vasSubjectNeck[a][b][1] == 3:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])
        if vasSubjectNeck[a][b][1] == 10:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])
        if vasSubjectNeck[a][b][1] == 30:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])
        if vasSubjectNeck[a][b][1] == 50:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])
        if vasSubjectNeck[a][b][1] == 100:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])
        if vasSubjectNeck[a][b][1] == 200:
            vas1.append(vasSubjectNeck[a][b][0])
            speed1.append(vasSubjectNeck[a][b][1])

        # FOREARM
        if vasSubjectForearm[a][b][1] == 3:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])
        if vasSubjectForearm[a][b][1] == 10:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])
        if vasSubjectForearm[a][b][1] == 30:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])
        if vasSubjectForearm[a][b][1] == 50:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])
        if vasSubjectForearm[a][b][1] == 100:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])
        if vasSubjectForearm[a][b][1] == 200:
            vas2.append(vasSubjectForearm[a][b][0])
            speed2.append(vasSubjectForearm[a][b][1])

plot1 = pd.DataFrame({'stimulation velocity': speed1, 'VAS score': vas1})
plot2 = pd.DataFrame({'stimulation velocity': speed2, 'VAS score': vas2})

# plt.subplot(1, 2, 1)
# sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot1, size=6, color='k')
# plt.yticks((-10, -5, 0, 5, 10))
# plt.ylabel("VAS score", labelpad=-5)
#
# plt.subplot(1, 2, 2)
# sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot2, size=6, color='k')
# plt.yticks((-10, -5, 0, 5, 10))
# plt.ylabel("VAS score", labelpad=-5)

plt.show()

#     print(temp)
#     for i in range(0, len(dataFrame)):
#         temp = dataFrame[headers[fields*u]][i]
#         if isinstance(temp, np.float):
#             vasResult.append(temp)
#     vasSubjectNeck
# print(vasResult)
# print(len(vasResult))
# print(counter)

# plt.figure()
