# script for Q-Q plot in python
# it generates a probability plot of sample data against the quantiles of a specefied theorical distribuition
# this case Normal distrinution.

import numpy as np
import pandas as pd

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')
headers = dataFrame.columns

# Setup
rng = np.random.RandomState(0)  # Seed RNG for replicability
# set initial conditions
trials = 5
fields = 6
subjects = 10

index_vas = 0  # back = 0; forearm = 2; tactor = 4;
index_speed = index_vas + 1

index = [0, 2, 4]
condition = [3, 10, 30, 50, 100, 200]

# storage
mean = []
sd = []
data = []


def fetch_data(subjects, trials, dataFrame, headers, condition, i, index_vas, index_speed):
    s1 = []
    for s in range(0, subjects):
        for t in range(0, trials * 6):
            if dataFrame[headers[(s * fields + index_speed)]][t] == condition[i]:
                s1.append(dataFrame[headers[s * fields + index_vas]][t])
                if len(s1) == (trials * subjects):
                    data.append(s1)
                    mean.append(np.mean(s1))
                    sd.append(np.std(s1))


speed = [3, 10, 30, 50, 100, 200]
for i in range(0, len(condition)):
    fetch_data(subjects, trials, dataFrame, headers, condition, i, index_vas, index_speed)

print(data)
print(mean)
print(sd)
