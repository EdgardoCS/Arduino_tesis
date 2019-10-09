import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_all')
headers = dataFrame.columns
sub_index = len(pd.read_excel(path, header=0, sheet_name='trials_all').columns)

# set initial conditions
trials = 5  # for each speed
fields = 6  # (vas, rnd) for each site
subjects = int(sub_index / fields)

print('number of subjects: ', subjects)

# since we are calculating the mean for each subject in all 3 sites
# its necessary to stablish the index of each score position
index = [2, 4]
color = ['b', 'g']
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
                    '''
                    print(condition[i])
                    print(s1)
                    print(np.mean(s1))
                    '''
                    mean.append(np.mean(s1))
                    sd.append(np.std(s1))


# the next cycle will move across the data and pass the info for each subject to fetch_data
for j in range(0, len(index)):
    index_vas = index[j]
    index_speed = index_vas + 1

    # create storage variables
    mean = []
    sd = []

    for i in range(0, len(condition)):
        fetch_data(trials, dataFrame, headers, condition, i, index_vas, index_speed)


    line_x = np.array(condition).reshape(-1, 1)
    line_y = np.array(mean)

    poly = PolynomialFeatures(degree=5)
    x_poly = poly.fit_transform(line_x)
    poly.fit(x_poly, line_y)
    lin2 = LinearRegression()
    lin2.fit(x_poly, line_y)

    plt.scatter(line_x, line_y, color=color[j])
    #plt.plot(line_x, lin2.predict(poly.fit_transform(line_x)), color=color[j])
    plt.xticks(condition)
    plt.xscale('log')
    # plt.errorbar(line_x, mean, sd, linestyle='None', ecolor=color[j], capsize=5)
    # plt.yticks((-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    plt.tight_layout()
    plt.legend(('Brush - antebrazo', 'Tactor - antebrazo'),
               loc='upper right')

