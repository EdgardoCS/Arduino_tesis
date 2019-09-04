import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_noTime')
headers = dataFrame.columns


# SORT DATA
def sortSecond(val):
    return val[1]


# set initial conditions
trials = 5
fields = 6
subjects = 9

# create variables
# temp

# storage
mean = []
sd = []

index_vas = 4  # back = 0; forearm = 2; tactor = 4;
index_speed = index_vas + 1
condition = [3, 10, 30, 50, 100, 200]


def fetch_data(subjects, trials, dataFrame, headers, condition, i):
    s1 = []
    for s in range(0, subjects):
        for t in range(0, trials * 6):
            if dataFrame[headers[(s * fields + index_speed)]][t] == condition[i]:
                s1.append(dataFrame[headers[s * fields + index_vas]][t])
                if len(s1) == (trials * subjects):
                    mean.append(np.mean(s1))
                    sd.append(np.std(s1))


for i in range(0, len(condition)):
    fetch_data(subjects, trials, dataFrame, headers, condition, i)

speed = [3, 10, 30, 50, 100, 200]

line_x = np.array(speed).reshape(-1, 1)
line_y = np.array(mean)

poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(line_x)
poly.fit(x_poly, line_y)
lin2 = LinearRegression()
lin2.fit(x_poly, line_y)

plt.scatter(line_x, line_y, color='k')
plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)), color='b')
plt.errorbar(line_x, mean, sd, linestyle='None', marker='o', ecolor='k', capsize=5)
# plt.yticks((-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
plt.tight_layout()
