#from base import Individual
from base.Tree import Tree
from base import Utils
from random import choice, randint, random
#import matplotlib.pyplot as plt
#from numpy import linspace

AbstractMethodError = NotImplementedError("You must override this method")

class Function():
    """Represents an individual in a population"""

    def __init__(self):
        """Construct a random individual."""
        self.tree = None
        self.depth = 0
        self.code = self.createLevel()
        self.tree = Tree()
        self.tree.createTree(self.code[:])

    @staticmethod
    def get_fitness(individual):
        """Return the fitness value for the given individual."""
        raise AbstractMethodError

    @staticmethod
    def mutate(individual, probability):
        """Mutate the given individual with the given probability."""
        raise AbstractMethodError

    @staticmethod
    def crossover(parent1, parent2):
        """Perform crossover with given parents."""
        raise AbstractMethodError

    @staticmethod
    def makecopy(individual):
        """Return a copy of the individual."""
        raise AbstractMethodError

    def createLevel(self):
        if self.depth < Utils.MAX_DEPTH:
            lis = [choice(Utils.OPERATORS), Utils.MARKER, Utils.MARKER]
        else:
            lis = [choice(Utils.ARG_0), Utils.MARKER, Utils.MARKER]

        if lis[0] in Utils.ARG_1:
            self.depth += 1
            tmp = self.createLevel()
            lis.pop(1)
            for ii in range(1, 1+len(tmp)):
                lis.insert(ii, tmp[ii-1])
            self.depth -= 1
        elif lis[0] in Utils.ARG_2:
            self.depth += 1
            tmp1 = self.createLevel()
            lis.pop(1)
            for ii in range(1, 1+len(tmp1)):
                lis.insert(ii, tmp1[ii-1])

            tmp2 = self.createLevel()
            lis.pop()
            for ii in range(0, len(tmp2)):
                lis.append(tmp2[ii])
            self.depth -= 1
        elif lis[0] == Utils.VAL:
            lis.pop(0)
            if Utils.INT:
                lis.insert(0, randint(Utils.MIN_VAL, Utils.MAX_VAL))
            else:
                lis.insert(0, random()*(Utils.MAX_VAL - Utils.MIN_VAL) + Utils.MIN_VAL)

        return lis

"""
funkcja = Function()
print(funkcja.code)
x = linspace(1, 20, 1000)
#print(x)
y = funkcja.tree.calculate(x)
#print(y)
plt.plot(x, y)
plt.show()
"""