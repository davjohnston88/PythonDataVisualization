import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set the chart title and label the axes
ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

# Set the size of the tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
