# matplotlib inline
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# read Data
data = pd.read_excel('fish.xlsx')
df = data[['age', 'length']]

x = df['age']
y = df['length']

# plot data
"""
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Scatter-plot of Length vs Age')
plt.scatter(x, y)
plt.show()
"""

# Distribution of data
"""
stdy = y.std()
meany = y.mean()
plt.hist(y)
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.title('Length Distribution Histogram')
print("The std of y is: " + str(stdy) + " The mean of y is: " + str(meany))

stdx = x.std()
meanx = x.mean()
plt.hist(x)
plt.xlabel('Age (yr)')
plt.ylabel('Quantity')
plt.title('Age Distribution Histogram')
print("The std of x is: " + str(stdx) + " The mean of x is: " + str(meanx))
"""

""" Linear Regression """
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
"""
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# print(p)
print('slope', slope, 'intercept', intercept)

sns.set(color_codes=True)


def lineFitLine(b):
    return intercept + slope * b


line = lineFitLine(x)
plt.scatter(x, y, color='b')
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Scatter plot of Length vs Age - Linear Regression')
plt.plot(x, line, c='g')
p = np.poly1d(np.polyfit(x, y, 2))
xp = np.linspace(1, 6, 100)
plt.plot(xp, p(xp), c='r')
plt.scatter(x, y)
plt.show()

r2_lin = r_value * r_value
print('Linear - The rsquared value is: ' + str(r2_lin))

r2 = r2_score(y, p(x))
print('Quadratic - The rsquared value is: ' + str(r2))
"""

""" Test Data """
# First, we need to divide the data into training and testing segments
# training data. used to create the model
# testing data. how well the model matches
# in this example, n1 (training data)  = 50, n2 (testing data)  = 28

shuffled = df.sample(frac=1).reset_index(drop=True)
shuffx = shuffled['age']
shuffy = shuffled['length']
trainX = shuffx[:50]
testX = shuffx[50:]
trainY = shuffy[:50]
testY = shuffy[50:]

"""
plt.scatter(trainX, trainY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Testing Data - Length vs Age')
axes = plt.axes()
axes.set_xlim([1, 6])
axes.set_ylim([50, 200])
plt.show()

plt.scatter(testX, testY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Testing Data - Length vs Age')
axes = plt.axes()
axes.set_xlim([1, 6])
axes.set_ylim([50, 200])
plt.show()
"""

# Create linear regression for the model
p1 = np.poly1d(np.polyfit(trainX, trainY, 1))
p1_1 = np.poly1d(np.polyfit(testX, testY, 1))
p2 = np.poly1d(np.polyfit(trainX, trainY, 2))
p2_2 = np.poly1d(np.polyfit(testX, testY, 2))
xp = np.linspace(0, 6, 100)
axes = plt.axes()
axes.set_xlim([1, 6])
axes.set_ylim([50, 200])

plt.subplot(221)
plt.scatter(trainX, trainY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Training Linear Regression')
plt.plot(xp, p1(xp), c='r')

r2_train1 = r2_score(trainY, p1(trainX))
print('Linear train', 'The rsquared value is: ' + str(r2_train1))

plt.subplot(222)
plt.scatter(testX, testY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Testing Linear Regression')
plt.plot(xp, p1_1(xp), c='r')

r2_test1 = r2_score(testY, p1_1(testX))
print('Linear test', 'The rsquared value is: ' + str(r2_test1))

plt.subplot(223)
plt.scatter(trainX, trainY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Training Quadratic Regression')
plt.plot(xp, p2(xp), c='r')

r2_train2 = r2_score(trainY, p2(trainX))
print('Quadratic train', 'The rsquared value is: ' + str(r2_train2))

plt.subplot(224)
plt.scatter(testX, testY)
plt.xlabel('Age (yr)')
plt.ylabel('Length (cm)')
plt.title('Testing Quadratic Regression')
plt.plot(xp, p2_2(xp), c='r')

r2_test2 = r2_score(testY, p2_2(testX))
print('Quadratic test', 'The rsquared value is: ' + str(r2_test2))

# plt.show()
