import matplotlib.pyplot as plt
import random

class Dice(object):
    def __init__(self):
        self.d = random.randint(1, 6)

class Sierpinski(Dice):
    def __init__(self, L,  number_of_iterations, current_pos_x, current_pos_y):
        self.L = L
        self.number_of_iterations = number_of_iterations
        self.current_pos_x = current_pos_x
        self.current_pos_y = current_pos_y
        self.P1x = L[0][0]
        self.P1y = L[0][1]
        self.P2x = L[1][0]
        self.P2y = L[1][1]
        self.P3x = L[2][0]
        self.P3y = L[2][1]
        Dice.__init__(self)
    def generate_data(self):
        self.X = []
        self.Y = []
        for i in range(self.number_of_iterations):
            d = Dice()
            if d.d == 1 or d.d == 2:
                self.current_pos_x = (self.P1x + self.current_pos_x)/2
                self.current_pos_y = (self.P1y + self.current_pos_y)/2
                self.X.append(self.current_pos_x)
                self.Y.append(self.current_pos_y)

            elif d.d == 3 or d.d == 4:
                self.current_pos_x = (self.P2x + self.current_pos_x)/2
                self.current_pos_y = (self.P2y + self.current_pos_y)/2
                self.X.append(self.current_pos_x)
                self.Y.append(self.current_pos_y)
            elif d.d == 5 or d.d == 6:
                self.current_pos_x = (self.P3x + self.current_pos_x)/2
                self.current_pos_y = (self.P3y + self.current_pos_y)/2
                self.X.append(self.current_pos_x)
                self.Y.append(self.current_pos_y)
        return self.X, self.Y

    def plot_data(self):
        plt.plot(self.X, self.Y, 'b.')
        plt.xlabel("Current Position 1")
        plt.ylabel("Current Position 2")
        plt.grid()
        plt.show()

def main():
    S = Sierpinski([[0, 0], [50, 50], [100, 0]], 100000, 1, 1)
    S.generate_data()
    S.plot_data()
main()