# calculation of time (in seconds) that elapsed between the stimulation is applied and the VAS
# score is register

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# set path
path = '../data/data_sub.xlsx'

dataFrame = pd.read_excel(path, header=2, sheet_name='trials_ex')
headers = dataFrame.columns

vasSubjectNeck = []
vasSubjectForearm = []
vasSubjectTactor = []

trials = 5
fields = 6
subjects = 5

speedNeck = []
speedForearm = []
speedTactor = []

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + 1)]][u] == 3:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])
        if dataFrame[headers[(t * fields) + 1]][u] == 10:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])
        if dataFrame[headers[(t * fields) + 1]][u] == 30:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])
        if dataFrame[headers[(t * fields) + 1]][u] == 50:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])
        if dataFrame[headers[(t * fields) + 1]][u] == 100:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])
        if dataFrame[headers[(t * fields) + 1]][u] == 200:
            vasSubjectNeck.append(dataFrame[headers[t * fields]][u])
            speedNeck.append(dataFrame[headers[(t * fields) + 1]][u])

        # stores the VAS score from each subject in the foreanr area using axidraw
        if dataFrame[headers[(t * fields) + 3]][u] == 3:
            vasSubjectForearm.append(dataFrame[headers[(t * fields) + 2]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])
        if dataFrame[headers[(t * fields) + 3]][u] == 10:
            vasSubjectForearm.append(dataFrame[headers[(t * fields) + 2]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])
        if dataFrame[headers[(t * fields) + 3]][u] == 30:
            vasSubjectForearm.append(dataFrame[headers[(t * fields + 2)]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])
        if dataFrame[headers[(t * fields) + 3]][u] == 50:
            vasSubjectForearm.append(dataFrame[headers[(t * fields + 2)]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])
        if dataFrame[headers[(t * fields) + 3]][u] == 100:
            vasSubjectForearm.append(dataFrame[headers[(t * fields + 2)]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])
        if dataFrame[headers[(t * fields) + 3]][u] == 200:
            vasSubjectForearm.append(dataFrame[headers[(t * fields + 2)]][u])
            speedForearm.append(dataFrame[headers[(t * fields) + 3]][u])

        # stores the VAS score from each subject in the foreanr area using tactors
        if dataFrame[headers[(t * fields) + 5]][u] == 3:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])
        if dataFrame[headers[(t * fields) + 5]][u] == 10:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])
        if dataFrame[headers[(t * fields) + 5]][u] == 30:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])
        if dataFrame[headers[(t * fields) + 5]][u] == 50:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])
        if dataFrame[headers[(t * fields) + 5]][u] == 100:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])
        if dataFrame[headers[(t * fields) + 5]][u] == 200:
            vasSubjectTactor.append(dataFrame[headers[(t * fields) + 4]][u])
            speedTactor.append(dataFrame[headers[(t * fields) + 5]][u])

fig1 = plt.figure(1)
plot1 = pd.DataFrame({'stimulation velocity': speedNeck, 'VAS score': vasSubjectNeck})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot1, size=6, color='k')
plt.title('VAS score vs AxiDraw Neck Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig1.show()

fig2 = plt.figure(2)
plot2 = pd.DataFrame({'stimulation velocity': speedForearm, 'VAS score': vasSubjectForearm})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot2, size=6, color='k')
plt.title('VAS score vs AxiDraw Forearm Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig2.show()

fig3 = plt.figure(3)
plot3 = pd.DataFrame({'stimulation velocity': speedTactor, 'VAS score': vasSubjectTactor})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot3, size=6, color='k')
plt.title('VAS score vs Tactor Forearm Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig3.show()
