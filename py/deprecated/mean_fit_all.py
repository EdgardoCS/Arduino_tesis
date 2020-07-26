import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../../data/parteI/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_available')
headers = dataFrame.columns
sub_index = len(pd.read_excel(path, header=0, sheet_name='trials_available').columns)

# set initial conditions
trials = 5  # for each speed
fields = 6  # (vas, rnd) for each site
subjects = int(sub_index / fields)

print('number of subjects: ', subjects)

# create storage variables
mean = []
sd = []

# since we are calculating the mean for each subject in all 3 sites
# its necessary to stablish the index of each score position
index = [0, 2, 4]
color = ['r', 'b', 'g']
condition = [3, 10, 30, 50, 100, 200]


# fetch_data will read the column for the specific subject at the specific position
# and storage the scores given the current speed
def fetch_data(trials, dataFrame, headers, condition, i, index_vas, index_speed):
    s1 = []
    for s in range(0, subjects):
        for t in range(0, trials * 6):
            if dataFrame[headers[(s * fields + index_speed)]][t] == condition[i]:
                s1.append(dataFrame[headers[s * fields + index_vas]][t])
                if len(s1) == (trials * subjects):
                    mean.append(np.mean(s1))
                    sd.append(np.std(s1))


# the next cycle will move across the data and pass the info for each subject to fetch_data
for j in range(0, len(index)):
    index_vas = index[j]
    index_speed = index_vas + 1
    mean = []
    sd = []
    for i in range(0, len(condition)):
        fetch_data(trials, dataFrame, headers, condition, i, index_vas, index_speed)

    '''
    line_x = np.array(condition).reshape(-1, 1)
    line_y = np.array(mean)

    poly = PolynomialFeatures(degree=5)
    x_poly = poly.fit_transform(line_x)
    poly.fit(x_poly, line_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, line_y)

    plt.scatter(line_x, line_y, color=color[j])
    plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)), color=color[j])
    plt.xticks(condition)
    # plt.errorbar(line_x, mean, sd, linestyle='None', marker='o', ecolor=color[j], capsize=5)
    # plt.yticks((-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    plt.xscale('log')
    plt.tight_layout()
    plt.legend(('Brush - espalda', 'Brush - antebrazo', 'Tactor - antebrazo'),
               loc='upper right')
    '''

    x_axis = [3, 10, 30, 50, 100, 200]
    y_axis = np.array(mean)
    z1 = np.polyfit(x_axis, y_axis, 2)
    p1 = np.poly1d(z1)
    xp = np.linspace(3, 200, 30)

    A = z1[0]
    B = z1[1]
    C = z1[2]

    max_x = (-B) / (2 * A)
    max_y = (A * (max_x ** 2)) + (B * max_x) + C  # Ax^2+Bx+C

    # plt.subplot(3, 5, a + 1)
    # plt.title('Sujeto ' + str(a + 1))
    # plt.ylim(-10, 10)
    plt.scatter(x_axis, y_axis)
    plt.plot(xp, p1(xp))
    plt.legend(('Brush - espalda', 'Brush - antebrazo', 'Tactor - antebrazo'),
               loc='upper right')
