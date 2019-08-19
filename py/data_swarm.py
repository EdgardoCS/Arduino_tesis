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

vasSubjectNeck1 = []
vasSubjectNeck2 = []
vasSubjectNeck3 = []
vasSubjectNeck4 = []
vasSubjectNeck5 = []
vasSubjectNeck6 = []

vasSubjectForearm1 = []
vasSubjectForearm2 = []
vasSubjectForearm3 = []
vasSubjectForearm4 = []
vasSubjectForearm5 = []
vasSubjectForearm6 = []

vasSubjectTactor1 = []
vasSubjectTactor2 = []
vasSubjectTactor3 = []
vasSubjectTactor4 = []
vasSubjectTactor5 = []
vasSubjectTactor6 = []

trials = 5
fields = 6
subjects = 5

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []

meanNeck = []
meanForearm = []
meanTactor = []
speedNeck = []
speedForearm = []
speedTactor = []

for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the neck area
        if dataFrame[headers[(t * fields + 1)]][u] == 3:
            # vasSubjectNeck1.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck1.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck1) == trials:
                temp1.append(vasSubjectNeck1)
                meanNeck.append(np.mean(temp1))
                speedNeck.append(3)
                vasSubjectNeck1 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 10:
            # vasSubjectNeck2.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck2.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck2) == trials:
                temp2.append(vasSubjectNeck2)
                meanNeck.append(np.mean(temp2))
                speedNeck.append(10)
                vasSubjectNeck2 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 30:
            # vasSubjectNeck3.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck3.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck3) == trials:
                temp3.append(vasSubjectNeck3)
                meanNeck.append(np.mean(temp3))
                speedNeck.append(30)
                vasSubjectNeck3 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 50:
            # vasSubjectNeck4.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck4.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck4) == trials:
                temp4.append(vasSubjectNeck4)
                meanNeck.append(np.mean(temp4))
                speedNeck.append(50)
                vasSubjectNeck4 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 100:
            # vasSubjectNeck5.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck5.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck5) == trials:
                temp5.append(vasSubjectNeck5)
                meanNeck.append(np.mean(temp5))
                speedNeck.append(100)
                vasSubjectNeck5 = []
        if dataFrame[headers[(t * fields) + 1]][u] == 200:
            # vasSubjectNeck6.append([dataFrame[headers[t * fields]][u], dataFrame[headers[(t * fields) + 1]][u]])
            vasSubjectNeck6.append(dataFrame[headers[t * fields]][u])
            if len(vasSubjectNeck6) == trials:
                temp6.append(vasSubjectNeck6)
                meanNeck.append(np.mean(temp6))
                speedNeck.append(200)
                vasSubjectNeck6 = []

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the foreanr area using axidraw
        if dataFrame[headers[(t * fields) + 3]][u] == 3:
            vasSubjectForearm1.append(dataFrame[headers[(t * fields) + 2]][u])
            if len(vasSubjectForearm1) == trials:
                temp1.append(vasSubjectForearm1)
                meanForearm.append(np.mean(temp1))
                speedForearm.append(3)
                vasSubjectForearm1 = []
        if dataFrame[headers[(t * fields) + 3]][u] == 10:
            vasSubjectForearm2.append(dataFrame[headers[(t * fields) + 2]][u])
            if len(vasSubjectForearm2) == trials:
                temp2.append(vasSubjectForearm2)
                meanForearm.append(np.mean(temp2))
                speedForearm.append(10)
                vasSubjectForearm2 = []
        if dataFrame[headers[(t * fields) + 3]][u] == 30:
            vasSubjectForearm3.append(dataFrame[headers[(t * fields + 2)]][u])
            if len(vasSubjectForearm3) == trials:
                temp3.append(vasSubjectForearm3)
                meanForearm.append(np.mean(temp3))
                speedForearm.append(30)
                vasSubjectForearm3 = []
        if dataFrame[headers[(t * fields) + 3]][u] == 50:
            vasSubjectForearm4.append(dataFrame[headers[(t * fields + 2)]][u])
            if len(vasSubjectForearm4) == trials:
                temp4.append(vasSubjectForearm4)
                meanForearm.append(np.mean(temp4))
                speedForearm.append(50)
                vasSubjectForearm4 = []
        if dataFrame[headers[(t * fields) + 3]][u] == 100:
            vasSubjectForearm5.append(dataFrame[headers[(t * fields + 2)]][u])
            if len(vasSubjectForearm5) == trials:
                temp5.append(vasSubjectForearm5)
                meanForearm.append(np.mean(temp5))
                speedForearm.append(100)
                vasSubjectForearm5 = []
        if dataFrame[headers[(t * fields) + 3]][u] == 200:
            vasSubjectForearm6.append(dataFrame[headers[(t * fields + 2)]][u])
            if len(vasSubjectForearm6) == trials:
                temp6.append(vasSubjectForearm6)
                meanForearm.append(np.mean(temp6))
                speedForearm.append(200)
                vasSubjectForearm6 = []

temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
for t in range(0, subjects):
    for u in range(0, len(dataFrame)):
        # stores the VAS score from each subject in the foreanr area using tactors
        if dataFrame[headers[(t * fields) + 5]][u] == 3:
            vasSubjectTactor1.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor1) == trials:
                temp1.append(vasSubjectTactor1)
                meanTactor.append(np.mean(temp1))
                speedTactor.append(3)
                vasSubjectTactor1 = []
        if dataFrame[headers[(t * fields) + 5]][u] == 10:
            vasSubjectTactor2.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor2) == trials:
                temp2.append(vasSubjectTactor2)
                meanTactor.append(np.mean(temp2))
                speedTactor.append(10)
                vasSubjectTactor2 = []
        if dataFrame[headers[(t * fields) + 5]][u] == 30:
            vasSubjectTactor3.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor3) == trials:
                temp3.append(vasSubjectTactor3)
                meanTactor.append(np.mean(temp3))
                speedTactor.append(30)
                vasSubjectTactor3 = []
        if dataFrame[headers[(t * fields) + 5]][u] == 50:
            vasSubjectTactor4.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor4) == trials:
                temp4.append(vasSubjectTactor4)
                meanTactor.append(np.mean(temp4))
                speedTactor.append(50)
                vasSubjectTactor4 = []
        if dataFrame[headers[(t * fields) + 5]][u] == 100:
            vasSubjectTactor5.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor5) == trials:
                temp5.append(vasSubjectTactor5)
                meanTactor.append(np.mean(temp5))
                speedTactor.append(100)
                vasSubjectTactor5 = []
        if dataFrame[headers[(t * fields) + 5]][u] == 200:
            vasSubjectTactor6.append(dataFrame[headers[(t * fields) + 4]][u])
            if len(vasSubjectTactor6) == trials:
                temp6.append(vasSubjectTactor6)
                meanTactor.append(np.mean(temp6))
                speedTactor.append(200)
                vasSubjectTactor6 = []
fig1 = plt.figure(1)
plot1 = pd.DataFrame({'stimulation velocity': speedNeck, 'VAS score': meanNeck})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot1, size=6, color='k')
plt.title('VAS score vs AxiDraw Neck Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig1.show()

fig2 = plt.figure(2)
plot2 = pd.DataFrame({'stimulation velocity': speedForearm, 'VAS score': meanForearm})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot2, size=6, color='k')
plt.title('VAS score vs AxiDraw Forearm Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig2.show()

fig3 = plt.figure(3)
plot3 = pd.DataFrame({'stimulation velocity': speedTactor, 'VAS score': meanTactor})
sns.swarmplot(x='stimulation velocity', y='VAS score', data=plot3, size=6, color='k')
plt.title('VAS score vs Tactor Forearm Stimulation')
plt.yticks((-10, -5, 0, 5, 10))
plt.ylabel("VAS score", labelpad=-5)
fig3.show()
