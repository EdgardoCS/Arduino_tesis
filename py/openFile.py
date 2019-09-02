import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = [3.0,
         6.0,
         2.0,
         5.0,
         3.0,
         6.0,
         2.0,
         7.0,
         2.0,
         4.0,
         3.0,
         5.0,
         8.0,
         2.0,
         2.0,
         3.0,
         3.0,
         3.0,
         3.0,
         5.0,
         7.0,
         3.0,
         5.0,
         4.0,
         4.0,
         2.0,
         2.0,
         0.0,
         6.0,
         2.0,
         ]
data2 = [3,
         10,
         200,
         30,
         100,
         50,
         200,
         10,
         100,
         3,
         50,
         30,
         10,
         50,
         100,
         3,
         200,
         30,
         100,
         30,
         10,
         200,
         3,
         50,
         3,
         100,
         30,
         200,
         10,
         50,
         ]

plt.scatter(data2, data1)
plt.xscale('log')
# plt.xticks((3, 10, 30, 50, 100, 200))
