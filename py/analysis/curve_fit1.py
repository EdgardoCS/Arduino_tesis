"""
Steps:
1. Get Data from each subject and condition
2. Calculate mean
3. Adjust curve and plot
4. Calculate statistical difference based on curve/intercept
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set desired column in dataFrame (index)
exp0 = [1, 2, 3]
exp1 = [1, 2]

# exp = exp2
exp = exp1

for i in range(13, 14):

    # set path
    path = '../../data/parteI/s(' + str(i) + ').xlsx'
    dataFrame = pd.read_excel(path, header=0, sheet_name='Hoja1')
    headers = dataFrame.columns

    store_data = []

    for d in exp:
        speed_column = 0
        vas_column = d
        x_axis = np.array(dataFrame[headers[0]])
        y_axis = np.array(dataFrame[headers[d]])

        xp = np.linspace(3, 200)

        z = np.polyfit(x_axis, y_axis, 2)
        p = np.poly1d(z)

        # plt.subplot(3, 5, i)
        plt.title('Sujeto ' + str(i))
        plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.05, hspace=0.23)

        if d == 1:
            plt.plot(xp, p(xp), 'b')  # , label='Espalda (brush)')
        # plt.plot(x_axis, y_axis, 'b.')
        elif d == 2:
            plt.plot(xp, p(xp), 'g')  # , label='Antebrazo (brush)')
        # plt.plot(x_axis, y_axis, 'g.')
        elif d == 3:
            plt.plot(xp, p(xp), 'k*-', label='Antebrazo (tactor)')
        # legend = plt.legend(loc='upper right', fontsize='x-large')
