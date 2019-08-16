# script for Q-Q plot in python
# it generates a probability plot of sample data against the quantiles of a specefied theorical distribuition
# this case Normal distrinution.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

nsample = 100
np.random.seed(7654321)

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

meanNeck = []
speedNeck = []

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + 1)]][u] == 3:
            vasSubjectNeck1.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck1) == trials:
                temp1.append(vasSubjectNeck1)
                meanNeck.append(np.mean(temp1))
                speedNeck.append(3)
                vasSubjectNeck1 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 10:
            vasSubjectNeck2.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck2) == trials:
                temp2.append(vasSubjectNeck2)
                meanNeck.append(np.mean(temp2))
                speedNeck.append(10)
                vasSubjectNeck2 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 30:
            vasSubjectNeck3.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck3) == trials:
                temp3.append(vasSubjectNeck3)
                meanNeck.append(np.mean(temp3))
                speedNeck.append(30)
                vasSubjectNeck3 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 50:
            vasSubjectNeck4.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck4) == trials:
                temp4.append(vasSubjectNeck4)
                meanNeck.append(np.mean(temp4))
                speedNeck.append(50)
                vasSubjectNeck4 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 100:
            vasSubjectNeck5.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck5) == trials:
                temp5.append(vasSubjectNeck5)
                meanNeck.append(np.mean(temp5))
                speedNeck.append(100)
                vasSubjectNeck5 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 200:
            vasSubjectNeck6.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck6) == trials:
                temp6.append(vasSubjectNeck6)
                meanNeck.append(np.mean(temp6))
                speedNeck.append(200)
                vasSubjectNeck6 = []

meanNeck.sort()

print(meanNeck)
# x = stats.norm.rvs(loc=0, scale=1, size=len(meanNeck))
res = stats.probplot(meanNeck, plot=plt)

plt.show()
