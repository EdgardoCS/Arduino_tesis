"""
Subject0
"""
import numpy as np
import matplotlib.pyplot as plt

speeds = [1, 2, 3, 4, 5, 6]
c1_1 = [10.0,
        -1.0,
        -5.0,
        -8.0,
        -10.0, ]
c1_2 = [9.0,
        9.0,
        -2.0,
        -8.0,
        -9.0
        ]
c1_3 = [10.0,
        9.0,
        4.0,
        2.0,
        3.0,
        ]
c1_4 = [9.0,
        2.0,
        5.0,
        5.0,
        1.0,
        ]
c1_5 = [9.0,
        1.0,
        1.0,
        1.0,
        1.0,
        ]
c1_6 = [8.0,
        7.0,
        1.0,
        -1.0,
        1.0,
        ]
c2_1 = [-5.0,
        3.0,
        5.0,
        -5.0,
        6.0
        ]
c2_2 = [9.0,
        9.0,
        5.0,
        1.0,
        5.0
        ]
c2_3 = [9.0,
        1.0,
        1.0,
        1.0,
        1.0
        ]
c2_4 = [7.0,
        1.0,
        -1.0,
        -8.0,
        1.0
        ]
c2_5 = [1.0,
        2.0,
        -8.0,
        7.0,
        -3.0
        ]
c2_6 = [1.0,
        7.0,
        -2.0,
        2.0,
        5.0
        ]

c3_1 = [-4.0, -4.0, -5.0, -4.0, -4.0]
c3_2 = [-1.0, -2.0, -2.0, -3.0, -3.0]
c3_3 = [4.0, 5.0, 5.0, 2.0, 3.0]
c3_4 = [2.0, 3.0, 1.0, 0.0, 3.0]
c3_5 = [3.0, 1.0, 2.0, 0.0, 2.0]
c3_6 = [1.0, 0.0, 0.0, 0.0, 0.0]

plt.plot(speeds, [c1_1, c1_2, c1_3, c1_4, c1_5, c1_6], 'k.')
plt.plot(speeds, [c2_1, c2_2, c2_3, c2_4, c2_5, c2_6], 'kx')
# plt.plot(speeds, [c3_1, c3_2, c3_3, c3_4, c3_5, c3_6], 'k*')

from scipy.optimize import curve_fit

x_axis = np.array(speeds)
y_axis1 = np.array([np.mean(c1_1), np.mean(c1_2), np.mean(c1_3), np.mean(c1_4), np.mean(c1_5), np.mean(c1_6)])
y_axis2 = np.array([np.mean(c2_1), np.mean(c2_2), np.mean(c2_3), np.mean(c2_4), np.mean(c2_5), np.mean(c2_6)])

# y_axis3 = np.array([np.mean(c3_1), np.mean(c3_2), np.mean(c3_3), np.mean(c3_4), np.mean(c3_5), np.mean(c3_6)])

z1 = np.polyfit(x_axis, y_axis1, 2)
p1 = np.poly1d(z1)

z2 = np.polyfit(x_axis, y_axis2, 2)
p2 = np.poly1d(z2)

xp = np.linspace(1, 6)
plt.plot(xp, p1(xp), 'k-', label='Espalda')
plt.plot(xp, p2(xp), 'k--', label='Antebrazo')
legend = plt.legend(loc='upper right', fontsize='x-large')
