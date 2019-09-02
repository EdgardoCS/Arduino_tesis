# the following script will plot a quadratic regression

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.switch_backend('TkAgg')
# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')

# path = '../data/data_sub0.xlsx'
# dataFrame = pd.read_excel(path, header=2, sheet_name='trials_ex')

headers = dataFrame.columns

vas1 = []
vas2 = []
vas3 = []
vas4 = []
vas5 = []
vas6 = []

trials = 5
fields = 6
subjects = 10

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

meanData = []
speedData = []


# SORT DATA
def sortSecond(val):
    return val[1]


# color = ['g', 'r', 'c', 'm', 'y', 'b']
for y in range(1, 3):
    index_vas = y + y * 1  # neck(0); forearm(2); tactor(4);
    index_speed = index_vas + 1

    # for t in range(0, subjects):
    for t in range(5, 6):
        for u in range(0, len(dataFrame)):
            # stores the VAS score from each subject in the neck area
            vas1.append(
                [dataFrame[headers[t * fields + index_vas]][u], dataFrame[headers[(t * fields + index_speed)]][u]])
            print(len(vas1))
