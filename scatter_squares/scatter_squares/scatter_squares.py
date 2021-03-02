import matplotlib.pyplot as plt

x_values = []
y_values = []

for i in range(1, 1000):
    x_values.append(i)
    y_values.append(i**2)
    
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring, edgecolor='none', s=50)

plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wartości", fontsize=14)

plt.axis([0, 1000, 0, 1000000])
plt.tick_params(axis='both', which='major', labelsize=10)

plt.savefig('squares_plot.png', bbox_inches='tight')

