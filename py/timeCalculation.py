# calculation of time (in seconds) that elapsed between the stimulation is applied and the VAS
# score is register

import numpy as np
import datetime
from datetime import timedelta

# set values from each trial duration
# trial1 = datetime.datetime.strptime('00:00:24', '%H:%M:%S').time()
trial1 = 24
trial2 = 7
trial3 = 3
trial4 = 2
trial5 = 1
trial6 = 1

startEach = []
startTemp = []
# interval = datetime.datetime.strptime('00:00:15', '%H:%M:%S').time() #grace
interval = 20

# read data from subject csv
path1 = '../data/sujetos/001/001_20190801_1057.csv'
# read the random position of each trial
path2 = '../data/rnd/trials.csv'

# extracts only the timestamp from subjects data
data1 = np.loadtxt(path1, dtype='str', delimiter=';', usecols=1)
# extracts random
data2 = np.loadtxt(path2, dtype='int', delimiter=';', usecols = 0)
# extracts start_time
data3 = np.loadtxt(path2,dtype = 'str', delimiter = ';', usecols= 1)

print(data1)
print(data2)
print(data3)

# start time for each stimulation
# only Grace
#start_time = datetime.datetime.strptime('10:48:15', '%H:%M:%S')
#startTemp.append(start_time)

# diff_time = startEach[0]+timedelta(seconds = interval)+timedelta(seconds= trial1)
# print(diff_time)
#for i in range(0, 30):
    # print(data2[i])

    # print(i)
    # if data2[i] == 3:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial1))
    # elif data2[i] == 10:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial2))
    # elif data2[i] == 30:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial3))
    # elif data2[i] == 50:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial4))
    # elif data2[i] == 100:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial5))
    # elif data2[i] == 200:
    #     startTemp.append(startTemp[i] + timedelta(seconds=interval) + timedelta(seconds=trial6))

#for i in startTemp:
    #startEach.append(i.time())
#print(len(startEach))
# if len(data1) == len(data2):
# prevent error from incongruent data
#for u, v in zip(startEach, data1):
    #print(u)
    #print(v)
    #print(u,v)

# # time1 = datetime.datetime.strptime(u, '%H:%M:%S').time()

# elapsed_time = time1-start_time
