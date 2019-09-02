import matplotlib.pyplot as plt
import numpy as np

bars = ('3', '10', '30', '50', '100', '200')
y_pos = np.arange(len(bars))
plt.figure(0)
data1 = [12, 19, 15, 12, 8, 6]  # brush
data2 = [24, 6, 14, 9, 7, 4]  # tactor
plt.bar(y_pos, data1
        , width=0.5)
plt.xticks(y_pos, bars)
plt.title('Subjects')
