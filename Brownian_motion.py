import math
import random
import matplotlib.pyplot as plt
import numpy


class BrownianMotion:
    def __init__(self, temp, nu, r, time, intervals, m):
        self.temp = temp
        self.nu = nu
        self.r = r
        self.k = 1.38e-23
        self.D = (self.k * self.temp) / (6 * math.pi * self.nu * self.r)
        self.time = time
        self.intervals = intervals
        self.interval = time / intervals
        self.cur_x = 0
        self.cur_y = 0
        self.lengths = []
        self.path = [self.cur_x, self.cur_y]
        self.m = m

    def random_angle(self):
        return random.randint(0, 360)

    def random_length(self, interval):
        return math.sqrt(2 * self.D * interval * random.uniform(0, 2))

    def find_step(self):
        angle = self.random_angle()
        length = self.random_length(self.interval)
        self.lengths.append(length)
        new_x = math.cos(angle) * length + self.cur_x
        new_y = math.sin(angle) * length + self.cur_y
        return [new_x, new_y]

    def plot_trajectory(self):
        for i in range(0, self.intervals):
            new_x, new_y = self.find_step()
            plt.scatter(self.cur_x, self.cur_y, marker='o', color='tab:blue')
            plt.plot([self.cur_x, new_x], [self.cur_y, new_y], color='tab:orange')
            self.cur_x, self.cur_y = new_x, new_y
        plt.scatter(self.cur_x, self.cur_y, marker='o', color='tab:blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.show()

    def calc_boltzmann(self):
        return (numpy.mean([i ** 2 for i in self.lengths]) * 3 * math.pi * self.nu * self.r) / \
               (self.temp * self.interval)

    # Вывод в см^2/c
    def find_diffusion(self):
        return self.D

    # Вывод в см
    def find_free_path(self):
        return 2 * self.D * math.sqrt((2 * self.k * self.temp)/self.m) * 100
