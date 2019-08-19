# script for Q-Q plot in python
# it generates a probability plot of sample data against the quantiles of a specefied theorical distribuition
# this case Normal distrinution.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

# Setup
rng = np.random.RandomState(0)  # Seed RNG for replicability

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

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + index_speed)]][u] == 3:
            vasSubjectNeck1.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck1) == trials:
                temp1.append(vasSubjectNeck1)
                meanData.append(np.mean(temp1))
                speedData.append(3)
                vasSubjectNeck1 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 10:
            vasSubjectNeck2.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck2) == trials:
                temp2.append(vasSubjectNeck2)
                meanData.append(np.mean(temp2))
                speedData.append(10)
                vasSubjectNeck2 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 30:
            vasSubjectNeck3.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck3) == trials:
                temp3.append(vasSubjectNeck3)
                meanData.append(np.mean(temp3))
                speedData.append(30)
                vasSubjectNeck3 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 50:
            vasSubjectNeck4.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck4) == trials:
                temp4.append(vasSubjectNeck4)
                meanData.append(np.mean(temp4))
                speedData.append(50)
                vasSubjectNeck4 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 100:
            vasSubjectNeck5.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck5) == trials:
                temp5.append(vasSubjectNeck5)
                meanData.append(np.mean(temp5))
                speedData.append(100)
                vasSubjectNeck5 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 200:
            vasSubjectNeck6.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubjectNeck6) == trials:
                temp6.append(vasSubjectNeck6)
                meanData.append(np.mean(temp6))
                speedData.append(200)
                vasSubjectNeck6 = []

n = len(meanData)

# Generate data with Normal distribution to be plotted against it
x = rng.normal(size=n)  # Sample 1: X ~ N(0, 1)

# Quantile-quantile plot
plt.figure()
plt.scatter(np.sort(x), np.sort(meanData))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.close()
