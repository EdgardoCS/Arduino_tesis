import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
from datetime import datetime, date

# GET DATA
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials')

# print(dataFrame)
headers = dataFrame.columns
# print(headers)
# print(len(headers))
time_elapsed1 = []
time_elapsed2 = []
time_elapsed3 = []
time_elapsed4 = []
time_elapsed5 = []
time_elapsed6 = []

# for b in range(0, 5):
for a in range(0, 30):
    if dataFrame[headers[2]][a] == 3:
        time_elapsed1.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))
    if dataFrame[headers[2]][a] == 10:
        time_elapsed2.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))
    if dataFrame[headers[2]][a] == 30:
        time_elapsed3.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))
    if dataFrame[headers[2]][a] == 50:
        time_elapsed4.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))
    if dataFrame[headers[2]][a] == 100:
        time_elapsed5.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))
    if dataFrame[headers[2]][a] == 200:
        time_elapsed6.append(int((str(datetime.combine(date.min, dataFrame[headers[1]][a]) -
                                      datetime.combine(date.min, dataFrame[headers[4]][a])).split(':')[2])))

# color = ['g', 'r', 'c', 'm', 'y', 'b']

# plt.plot(time_elapsed1, color='g')
# plt.plot(time_elapsed2, color='r')
# plt.plot(time_elapsed3, color='c')
# plt.plot(time_elapsed4, color='m')
# plt.plot(time_elapsed5, color='y')
# plt.plot(time_elapsed6, color='b')
# plt.show()
