# the following script will plot a quadratic regression

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def plot_data(mean, sd, color):
    speed = [3, 10, 30, 50, 100, 200]
    line_x = np.array(speed).reshape(-1, 1)
    line_y = np.array(mean)

    poly = PolynomialFeatures(degree=4)
    x_poly = poly.fit_transform(line_x)
    poly.fit(x_poly, line_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, line_y)

    # plt.scatter(line_x, line_y, color=color)
    plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)), color=color)
    # plt.errorbar(line_x, mean, sd, linestyle='None', marker='o', ecolor='k', capsize=5)
    # plt.yticks((-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    plt.tight_layout()
    plt.legend(('Brush - espalda', 'Brush - antebrazo', 'Tactors - antebrazo'),
               loc='upper right')


mean1 = [1.7777777777777777, 2.066666666666667, 2.2444444444444445, 1.8888888888888888, 0.9777777777777777,
         -0.06666666666666667]
sd1 = [3.2103228559610906, 3.440930106817051, 2.310897426018785, 2.442423406939393, 2.1958434359174444,
       2.8158282775923835]
mean2 = [1.1555555555555554, 2.111111111111111, 2.5555555555555554, 2.111111111111111, 1.3555555555555556,
         0.5333333333333333]
sd2 = [3.72353210782782, 3.5479084431517753, 2.879471830855679, 2.301904740013966, 2.222666622231109, 2.517494345133228]
mean3 = [0.5555555555555556, 1.3555555555555556, 2.0, 1.2444444444444445, 0.24444444444444444, -0.3111111111111111]
sd3 = [4.933133129070795, 3.163370604315421, 1.8012341448141729, 1.727625931162383, 1.7147148198987046,
       1.5176329847967887]

_color = ['r', 'b', 'g']
_mean = [mean1, mean2, mean3]
_sd = [sd1, sd2, sd3]

for u in range(0, 3):
    mean = _mean[u]
    sd = _sd[u]
    color = _color[u]
    plot_data(mean, sd, color)
