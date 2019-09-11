import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_time')
headers = dataFrame.columns

# set initial conditions
trials = 5
fields = 10
subjects = 7

index = [2, 7]
color = ['r', 'b']
condition = [3, 10, 30, 50, 100, 200]


def fetch_time(subjects, condition, i, index_resp, index_speed, index_end):
    temp = []
    for s in range(0, subjects):
        for a in range(0, 30):
            if dataFrame[headers[(s * fields + index_speed)]][a] == condition[i]:
                # we want to store all time elapsed for each speed
                temp.append(
                    int((str(datetime.combine(date.min, dataFrame[headers[(s * fields + index_resp)]][a]) -
                             datetime.combine(date.min, dataFrame[headers[(s * fields + index_end)]][a])).split(':')[
                        2]))
                )
                if len(temp) == (trials * subjects):
                    time_mean.append(np.mean(temp))
                    time_sd.append(np.std(temp))


for j in range(0, len(index)):
    index_speed = index[j]
    index_resp = index_speed - 1
    index_end = index_speed + 2

    time_mean = []
    time_sd = []
    for i in range(0, len(condition)):
        fetch_time(subjects, condition, i, index_resp, index_speed, index_end)

    print(time_mean)

    # attempt to fit
    line_x = np.array(condition).reshape(-1, 1)
    line_y = np.array(time_mean)

    poly = PolynomialFeatures(degree=5)
    x_poly = poly.fit_transform(line_x)
    poly.fit(x_poly, line_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, line_y)

    plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)), color=color[j])
    plt.scatter(condition, time_mean, color=color[j])
    plt.errorbar(condition, time_mean, time_sd, linestyle='None', marker='o', ecolor=color[j], capsize=5)
    plt.tight_layout()
    plt.legend(('Brush - espalda', 'Brush - antebrazo'),
               loc='upper right')
