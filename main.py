from base.Population import Population
from Function import Function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
points = np.array([x, x])
points[1] = np.log(x)
population = Population(100, Function, points)
plt.plot(points[0], points[1], 'b*')

for i in range(0, 10):
    best = population.advance_step()
    plt.plot(best.x, best.y)
plt.show()
