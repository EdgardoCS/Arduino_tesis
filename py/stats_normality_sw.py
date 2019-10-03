from scipy.stats import shapiro

# '''
import numpy as np
import pandas as pd
import pylab
import scipy.stats as stats

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_all')
headers = dataFrame.columns
sub_index = len(pd.read_excel(path, header=0, sheet_name='trials_all').columns)

# set initial conditions
trials = 5  # for each speed
fields = 6  # (vas, rnd) for each site
subjects = int(sub_index / fields)

# we need to obtain the raw data for each subject at each site
# index = [0, 2, 4]
index = [2, 4]
condition = [3, 10, 30, 50, 100, 200]


# fetch_data will read the column for the specific subject at the specific position
# and storage the scores given the current speed
def shapiro_normality_check(raw_data):
    stat, p = shapiro(raw_data)
    print('statics=%.3f, p=%.3f' % (stat, p))
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')


def qq_normality_check(raw_data):
    stats.probplot(raw_data, dist="norm", plot=pylab)
    pylab.show()


def fetch_data(trials, dataFrame, headers, condition, i, index_vas, index_speed):
    s1 = []
    for s in range(0, subjects):
        for t in range(0, trials * 6):
            if dataFrame[headers[(s * fields + index_speed)]][t] == condition[i]:
                s1.append(dataFrame[headers[s * fields + index_vas]][t])
                if len(s1) == (trials * subjects):
                    raw_data = s1
                    if i == 5:
                        shapiro_normality_check(raw_data)
                        # qq_normality_check(raw_data)


# the next cycle will move across the data and pass the info for each subject to fetch_data
for j in range(0, len(index)):
    index_vas = index[j]
    index_speed = index_vas + 1
    for i in range(0, len(condition)):
        fetch_data(trials, dataFrame, headers, condition, i, index_vas, index_speed)
