# calculation of time (in seconds) that elapsed between the stimulation is applied and the VAS
# score is register

import time
import datetime
import numpy as np
import pandas as pd
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
fields = 11

subjects = 3

# print(dataFrame[headers[2]])
for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        vasResult1.append(dataFrame[headers[t * fields]][u])
    vasSubjectNeck.append(vasResult1)
    for u in range(0, len(dataFrame)):
        vasResult2.append(dataFrame[headers[(t * fields)+4]][u])
    vasSubjectForearm.append(vasResult2)
    for u in range(0, len(dataFrame)):
        vasResult3.append(dataFrame[headers[(t * fields)+8]][u])
    vasSubjectTactor.append(vasResult3)
print(vasSubjectNeck)
print(vasSubjectForearm)
print(vasSubjectTactor)


#     print(temp)
#     for i in range(0, len(dataFrame)):
#         temp = dataFrame[headers[fields*u]][i]
#         if isinstance(temp, np.float):
#             vasResult.append(temp)
#     vasSubjectNeck
# print(vasResult)
# print(len(vasResult))
# print(counter)

plt.figure()