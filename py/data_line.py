import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set path
path = '../data/data_sub.xlsx'
dataFrame = pd.read_excel(path, header=2, sheet_name='trials_ex')
headers = dataFrame.columns

trials = 5
fields = 11
subjects = 4

vasSubjectNeck1 = []
vasSubjectNeck2 = []
vasSubjectNeck3 = []
vasSubjectNeck4 = []
vasSubjectNeck5 = []
vasSubjectNeck6 = []

meanNeck = []
vasSpeed = [3, 10, 30, 50, 100, 200]

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        if dataFrame[headers[(t * fields) + 2]][u] == 3:
            vasSubjectNeck1.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck1) == trials:
                meanNeck.append([np.mean(vasSubjectNeck1), 3])
                # print(meanNeck)
                vasSubjectNeck1 = []
        if dataFrame[headers[(t * fields) + 2]][u] == 10:
            vasSubjectNeck2.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck2) == trials:
                meanNeck.append([np.mean(vasSubjectNeck2), 10])
                vasSubjectNeck2 = []
        if dataFrame[headers[(t * fields) + 2]][u] == 30:
            vasSubjectNeck3.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck3) == trials:
                meanNeck.append([np.mean(vasSubjectNeck3), 30])
                vasSubjectNeck3 = []
        if dataFrame[headers[(t * fields) + 2]][u] == 50:
            vasSubjectNeck4.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck4) == trials:
                meanNeck.append([np.mean(vasSubjectNeck4), 50])
                vasSubjectNeck4 = []
        if dataFrame[headers[(t * fields) + 2]][u] == 100:
            vasSubjectNeck5.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck5) == trials:
                meanNeck.append([np.mean(vasSubjectNeck5), 100])
                vasSubjectNeck5 = []
        if dataFrame[headers[(t * fields) + 2]][u] == 200:
            vasSubjectNeck6.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck6) == trials:
                meanNeck.append([np.mean(vasSubjectNeck6), 200])
                vasSubjectNeck6 = []
        if len(meanNeck) == 6:
            plot1 = pd.DataFrame({'stimulation velocity': vasSpeed, 'VAS score': [meanNeck[0][0], meanNeck[1][0], meanNeck[2][0], meanNeck[3][0], meanNeck[4][0], meanNeck[5][0]]})
            plt.plot(vasSpeed,
                 [meanNeck[0][0], meanNeck[1][0], meanNeck[2][0], meanNeck[3][0], meanNeck[4][0], meanNeck[5][0]])
            plt.yticks((-10, -5, 0, 5, 10))
            #plt.xticks((3, 10, 30, 50, 100, 200))
            meanNeck = []


#print(meanNeck)
#print(meanNeck[0][0])
