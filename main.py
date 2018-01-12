import base.Population
import Function
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(1, 11)
points = np.log(x)
population = base.Population(100, Function, [x1, points])

for i in range(0, 10):
    best = population.advance_step()
    x = np.linspace(1, 20, 1000)
    y = best.tree.calculate(x)
    plt.plot(x1, points, 'b*')
    plt.plot(x, y)
plt.show()