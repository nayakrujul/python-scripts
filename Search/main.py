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
    x.append(int(row[0]))
    y.append(float(row[1]))

x, y = np.array(x), np.array(y)

ax.plot(x, y, '#FFA500', label='Binary search')

a, b = np.polyfit(x, y, 1)
plt.plot(x, (a * x) + b, '#FF0000', label='Binary search best fit')

x, y = [], []

for row in data:
    x.append(int(row[0]))
    y.append(float(row[2]))

x, y = np.array(x), np.array(y)

ax.plot(x, y, '#00FF00', label='Linear search')

a, b = np.polyfit(x, y, 1)
plt.plot(x, (a * x) + b, '#228B22', label='Linear search best fit')

plt.xlabel('Number of elements in the list')
plt.ylabel('Average time to complete in milliseconds')

plt.legend()
plt.show()