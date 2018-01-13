from base.Population import Population
from Function import Function
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1, 11)
x = np.linspace(1, 10, 20)
points = np.array([x, x])
points[1] = x * np.sin(x) * 5
population = Population(200, Function, points)
plt.plot(points[0], points[1], 'b*')
maximum = 0
plots = []
max_difference = len(points[1])
print("Max fitness = %f" % max_difference)
for i in range(0, 100):
    # print("=" * 10 + str(i) + "=" * 10)
    # for x in population.individuals:
    #     print(x.code)
    #     print(Function.get_fitness(x))
    best = population.advance_step()

    fitness = Function.get_fitness(best)
    # print(fitness)
    if fitness > maximum:
        print("Better at %d: fitness = %f" % (i, fitness))
        plots.append(str(i))
        maximum = fitness
        plt.plot(best.x, best.y)

plt.ylim(min(points[1])-5, max(points[1])+5)
plt.legend(["Dane"] + plots)
plt.show()
