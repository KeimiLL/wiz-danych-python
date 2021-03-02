import matplotlib.pyplot as plt

x_values = []
y_values = []

for i in range(1, 5001):
    x_values.append(i)
    y_values.append(i*i*i)
    
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.summer, edgecolor='none', s=20)

plt.title("Sześciany liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Sześciany wartości", fontsize=14)

plt.axis([0, 5000, 0, 125000000000])
plt.tick_params(axis='both', which='major', labelsize=10)

plt.savefig('szesciany_plot.png', bbox_inches='tight')