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

ax.plot(np.array(x), np.array(y), label='Bubble sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[2]))

ax.plot(np.array(x), np.array(y), label='Bucket sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[3]))

ax.plot(np.array(x), np.array(y), label='Insertion sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[4]))

ax.plot(np.array(x), np.array(y), label='Quick sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[5]))

ax.plot(np.array(x), np.array(y), label='Radix sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[6]))

ax.plot(np.array(x), np.array(y), label='Selection sort')

x, y = [], []

for row in data:
    x.append(float(row[0]))
    y.append(float(row[7]))

ax.plot(np.array(x), np.array(y), label='Comb sort')

plt.xlabel('Number of elements in the list')
plt.ylabel('Average time to sort in milliseconds')

plt.legend()
plt.show()