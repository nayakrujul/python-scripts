import matplotlib.pyplot as plt
import numpy as np


f = open('times.csv')
lines = f.read().split('\n')
f.close()

data = []
for line in lines:
    data.append(line.split(', '))


fig, ax = plt.subplots()

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[1]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[2]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[3]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[4]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[5]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[6]))

ax.plot(np.array(x), np.array(y))

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[7]))

ax.plot(np.array(x), np.array(y))

print(
    'Blue = Bubble sort',
    'Orange = Bucket sort',
    'Green = Insertion sort',
    'Red = Quick sort',
    'Purple = Radix sort',
    'Brown = Selection sort',
    'Pink = Comb sort',
    '\nX axis: Number of elements in the list',
    '\nY axis: Average time to sort in milliseconds',
    sep='\n'
)

plt.show()