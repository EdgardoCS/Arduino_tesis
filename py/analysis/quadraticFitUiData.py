"""
The following will read the data from each subject xlsx file. then using polifyt it will calculate the quadratic regression.
plot grid : 2x3
Blue: FOREARM (MultiTAC)
Green: FOREARM (TACTORS)

Steps:
1. Get Data from each subject and condition
2. Calculate mean
3. Adjust curve and plot
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set desired column in dataFrame (index)
exp1 = [1, 2]

for i in range(1, 6):

    # set path
    path = '../../data/uiData/s (' + str(i) + ').xlsx'
    dataFrame = pd.read_excel(path, header=0, sheet_name='Hoja1')
    headers = dataFrame.columns

    store_data = []

    for d in exp1:
        speed_column = 0
        vas_column = d
        x_axis = np.array(dataFrame[headers[0]])
        y_axis = np.array(dataFrame[headers[d]])

        xp = np.linspace(3, 200)

        z = np.polyfit(x_axis, y_axis, 2)
        p = np.poly1d(z)

        plt.subplot(2, 3, i)
        plt.title('Sujeto ' + str(i))
        plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.05, hspace=0.23)

        if d == 1:
            plt.plot(xp, p(xp), 'b')
        elif d == 2:
            plt.plot(xp, p(xp), 'g')