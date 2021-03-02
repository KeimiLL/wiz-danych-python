import matplotlib.pyplot as plt
from random_walk2 import RandomWalk

#Tworzenie nowego błądzenia losowego dopóki program pozostaje aktywny.

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    #Określenie wielkości okna wykresu.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=0.5)

    #Podświetlenie pierwszego i ostatniego punktu błądzenia losowego.
    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75)

    #Ukrycie osi.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Utworzyc kolejne bladzenie losowe? (t/n): ")
    if keep_running == 'n':
        break
