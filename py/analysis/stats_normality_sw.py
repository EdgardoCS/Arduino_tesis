from scipy.stats import shapiro

# '''
import numpy as np
import pandas as pd
import pylab
import scipy.stats as stats

# GET DATA
forearm_mean = [1.0, 2.3, 2.8, 2.5, 1.8, 1.1]
back_mean = [0.9, 2.1, 2.6, 2.1, 1.5, 0.6]
forearm2_mean = [1.3, 2.3, 2.1, 1.3, 0.4, -0.1]

condition = [3, 10, 30, 50, 100, 200]


# fetch_data will read the column for the specific subject at the specific position
# and storage the scores given the current speed
def shapiro_normality_check(raw_data):
    stat, p = shapiro(raw_data)
    # print('statics=%.3f, p=%.3f' % (stat, p))
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')


shapiro_normality_check(back_mean)
shapiro_normality_check(forearm_mean)
shapiro_normality_check(forearm2_mean)
