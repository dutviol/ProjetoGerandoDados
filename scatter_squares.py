import matplotlib.pyplot as plt

x_values = list(range(1, 100))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap='Blues', edgecolor = 'none', s = 40)


plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 5)
 
plt.show()
