import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()

rw.fill_walk()

point_numbers = list(range(rw.num_points))

plt.figure(figsize = (10,6))

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = 'Blues', edgecolor ='none', s = 1)

plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor = 'none', s=10)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor = 'none', s=10)

# Removendo os eixos
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)



plt.show()