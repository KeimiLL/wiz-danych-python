from random import choice

class RandomWalk():
    """Klasa przeznaczona do wygenerowania błądzenia losowego."""

    def __init__(self, num_points=5000):
        """Inicjalizacja atryutów błądzenia."""
        self.num_points = num_points

        #Punkt początkowy ma współrzędne (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Ustalenie kierunku i odległości dla danego kroku i przygotowanie tego kroku"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów dla błądzenia losowego."""

        #Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów.
        while len(self.x_values) < self.num_points:
            #Ustalenie kierunku oraz odległości do pokonania w tym kierunku
            x_step = self.get_step()
            y_step = self.get_step()
            #Odrzucenie ruchów, które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue
            #Ustalenie następnych wartości X i Y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
