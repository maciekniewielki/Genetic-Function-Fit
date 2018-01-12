import base.Population
import Function
import numpy as np
import matplotlib.pyplot as plt

points = np.log(np.arange(1, 11))
population = base.Population(100, Function, points)

for i in range(1, 10):
    best = population.advance_step()
    x = np.linspace(1, 20, 1000)
    y = best.tree.calculate(x)
    plt.plot(x, y)