import numpy as np
import matplotlib.pyplot as plt

'The following will calculate the quadratic regression for both VAS ratings using brush stimulation'
'also, it calculates the maximum speed for the curve'

speeds = [3, 10, 30, 50, 100, 200]

data = [[0.9, 2.1, 2.6, 2.1, 1.5, 0.6], [1.0, 2.3, 2.8, 2.5, 1.8, 1.1]]
# plt.plot(speeds, data[0], 'k.')
# plt.plot(speeds, data[1], 'kx')

x_axis = np.array(speeds)
for a in range(0, 2):
    y_axis = np.array(data[a])

    z = np.polyfit(x_axis, y_axis, 2)
    p = np.poly1d(z)

    A = z[0]
    B = z[1]
    C = z[2]
    x_point = (-B) / (2 * A)
    xp = np.linspace(3, 200)

    print(z)
    print(p)
    if a == 0:
        plt.plot(xp, p(xp), 'k--', label='brush - back')
        print('max speed back', x_point)
    if a == 1:
        plt.plot(xp, p(xp), 'k-', label='brush - forearm')
        print('max speed forearm', x_point)
    legend = plt.legend(loc='upper right', fontsize='x-large')
    plt.xticks([3, 10, 30, 50, 100, 200])
