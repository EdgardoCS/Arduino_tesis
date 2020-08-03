import numpy as np

data1 = [
    3, 4, 3, 5, 4,
    6, 7, 8, 7, 6,
    5, 5, 3, 5, 2,
    6, 3, 2, 4, 2,
    3, 2, 2, 3, 2,
    2, 2, 3, 3, 0]
vel1 = [
    3, 3, 3, 3, 3,
    10, 10, 10, 10, 10,
    30, 30, 30, 30, 30,
    50, 50, 50, 50, 50,
    100, 100, 100, 100, 100,
    200, 200, 200, 200, 200,
]
x1 = np.array(vel1)
y1 = np.array(data1)

data2 = [
    3.8, 6.8, 4.0, 3.4, 2.4, 2.0
]
vel2 = [
    3, 10, 30, 50, 100, 200
]

x2 = np.array(vel2)
y2 = np.array(data2)

p1 = np.poly1d(np.polyfit(x1, y1, 2))
p2 = np.poly1d(np.polyfit(x2, y2, 2))

print(p1)
print(p2)
