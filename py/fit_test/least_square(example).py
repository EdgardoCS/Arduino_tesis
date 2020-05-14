import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Steps. 
1. Read data
2. Determine independent and dependent variables (X,Y) 
3. Calculate slope and intercept (m,c) 
4. Plot
5. Evaluate model

"""
# Reading Data
path = 'head.csv'
data = pd.read_csv(path)

# Computing X and Y
X = data['Head Size(cm^3)'].values  # independent variable
Y = data['Brain Weight(grams)'].values  # dependent variable

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

num = 0
den = 0
for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2
    m = num / den
    c = mean_y - (m * mean_x)

# Printing coefficients
print("Coefficients")
print(m, c)

# Plotting Values and Regression Line

max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x

"""
# Plotting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Plotting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
"""

# Calculating Root Mean Squares Error
rootMeanSquareError = 0
for i in range(n):
    y_pred = c + m * X[i]
    rootMeanSquareError += (Y[i] - y_pred) ** 2
rootMeanSquareError = np.sqrt(rootMeanSquareError / n)
print("RMSE")
print(rootMeanSquareError)

# Calculating R2 Score
ss_tot = 0
ss_res = 0
for i in range(n):
    y_pred = c + m * X[i]
    ss_tot += (Y[i] - mean_y) ** 2
    ss_res += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_res/ss_tot)
print("R2 Score")
print(r2)

