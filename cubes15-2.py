import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set the chart title and label the axes
ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

# Set the size of the tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
