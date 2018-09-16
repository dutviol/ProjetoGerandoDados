import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(5000)

rw.fill_walk()

plt.figure(figsize =(10,5))
plt.plot(rw.x_values, rw.y_values, linewidth = 2)

plt.scatter(rw.x_values[0],rw.y_values[0], c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.show()