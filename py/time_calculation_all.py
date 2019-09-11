import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials')
headers = dataFrame.columns

# set initial conditions
trials = 5
fields = 6
subjects = 10

condition = [3, 10, 30, 50, 100, 200]
time_mean = []
time_sd = []


for i in range(0, len(condition)):
    temp = []
    for a in range(0, trials * fields):
        if dataFrame[headers[7]][a] == condition[i]:
            # we want to store all time elapsed for each speed
            temp.append(
                int((str(datetime.combine(date.min, dataFrame[headers[6]][a]) -
                         datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2]))
            )
            if len(temp) == trials:
                time_mean.append(np.mean(temp))
                time_sd.append(np.std(temp))

# attempt to fit


'''
line_x = np.array(condition).reshape(-1, 1)
line_y = np.array(time_mean)

poly = PolynomialFeatures(degree=5)
x_poly = poly.fit_transform(line_x)
poly.fit(x_poly, line_y)
lin2 = LinearRegression()
lin2.fit(x_poly, line_y)

plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)))
#
plt.scatter(condition, time_mean)
plt.errorbar(condition, time_mean, time_sd, linestyle='None', marker='o', capsize=5)
'''