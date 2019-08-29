# script for Q-Q plot in python
# it generates a probability plot of sample data against the quantiles of a specefied theorical distribuition
# this case Normal distrinution.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Setup
rng = np.random.RandomState(0)  # Seed RNG for replicability

# Set data
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')
<<<<<<< HEAD
=======

>>>>>>> 87f9fbc92740f1525fd60e3fb6a047e422be0bec
headers = dataFrame.columns

# Define variables
vasSubject1 = []
vasSubject2 = []
vasSubject3 = []
vasSubject4 = []
vasSubject5 = []
vasSubject6 = []

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

meanData = []
speedData = []

# Set initial conditions
trials = 5
fields = 6  # 3-10-30-50-100-200
subjects = 8  # number of subjects

index_vas = 0  # neck(0); forearm(2); tactor(4);
index_speed = index_vas + 1  # position of rnd values

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + index_speed)]][u] == 3:
            vasSubject1.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject1) == trials:
                temp1.append(vasSubject1)
                meanData.append(np.mean(temp1))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject1 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 10:
            vasSubject2.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject2) == trials:
                temp2.append(vasSubject2)
                meanData.append(np.mean(temp2))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject2 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 30:
            vasSubject3.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject3) == trials:
                temp3.append(vasSubject3)
                meanData.append(np.mean(temp3))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject3 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 50:
            vasSubject4.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject4) == trials:
                temp4.append(vasSubject4)
                meanData.append(np.mean(temp4))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject4 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 100:
            vasSubject5.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject5) == trials:
                temp5.append(vasSubject5)
                meanData.append(np.mean(temp5))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject5 = []
        if dataFrame[headers[(t * fields) + index_speed]][u] == 200:
            vasSubject6.append(dataFrame[headers[t * fields + index_vas]][u])
            if len(vasSubject6) == trials:
                temp6.append(vasSubject6)
                meanData.append(np.mean(temp6))
                speedData.append(dataFrame[headers[(t * fields + index_speed)]][u])
                vasSubject6 = []

# Generate data with Normal distribution to be plotted against it
# n = len(meanData)
# x = rng.normal(size=n)  # Sample 1: X ~ N(0, 1)

# Check for values
# print(meanData)
# print(np.sort(meanData))
# print(x)
# print(np.sort(x))

# Quantile-quantile plot
plt.figure()
# plt.scatter(np.sort(x), np.sort(meanData))
stats.probplot(np.sort(meanData), dist='norm', plot=plt)
plt.title('Difference Q-Q Plot')
plt.show()

# plt.close()
