#from base import Individual
from base.Tree import Tree
from base import Utils
import random
import matplotlib.pyplot as plt
from numpy import linspace, isnan, isfinite
from math import sqrt

AbstractMethodError = NotImplementedError("You must override this method")


class Function():
    """Represents an individual in a population"""

    def __init__(self):
        """Construct a random individual."""
        self.fitness = None
        self.changed = False
        self.tree = None
        self.depth = 0
        self.code = self.createLevel()
        self.tree = Tree()
        self.tree.createTree(self.code[:])
        x = linspace(1, 20, 1000)
        self.x = x
        self.y = self.tree.calculate(x)
        while isnan(self.y).any() or not isfinite(self.y).all():
            self.code.clear()
            self.code = self.createLevel()
            self.tree.delete_tree()
            self.tree.createTree(self.code[:])
            self.y = self.tree.calculate(x)


    @staticmethod
    def get_fitness(individual, points):
        """Return the fitness value for the given individual."""

        if individual.fitness and not individual.changed:
            return individual.fitness

        def get_length(x, y):
            _sum = 0
            for ii in range(len(x)-1):
                _sum += sqrt((x[ii+1] - x[ii])**2 + (y[ii+1] - y[ii])**2)
            return _sum

        optimal_length = get_length(points[0], points[1])
        real_length = get_length(individual.x[:-100], individual.y[:-100])

        _sum = 0
        for ii in range(len(points[1])):
            _sum += abs(points[1][ii] - individual.y[100*ii])

        # if optimal_length > real_length:
        #     print("Optimal: %f, real: %f" % (optimal_length, real_length))
        max_difference = (max(points[1]) - min(points[1])) * len(points[1])
        individual.fitness = (max_difference - _sum) * sqrt(min(optimal_length/real_length, 1))
        if individual.fitness < 0:
            individual.fitness = 0
        individual.changed = False

        return individual.fitness

    @staticmethod
    def mutate(individual):
        """Mutate the given individual with the given probability."""
        dep = random.randint(1, Utils.MAX_DEPTH)
        curtree = individual.tree
        for i in range(0, dep):
            direction = random.random()
            if direction < 0.5:
                if curtree.left:
                    curtree = curtree.left
                else:
                    break
            else:
                if curtree.right:
                    curtree = curtree.right
                else:
                    break
        if curtree.left and curtree.right:
            list = Utils.ARG_2
            list.remove(curtree.data)
            curtree.data = random.choice(list)

        elif curtree.left:
            list = Utils.ARG_1
            list.remove(curtree.data)
            curtree.data = random.choice(list)

        else:
            varval = random.random()
            if curtree.data == Utils.VAR or varval < 0.5:
                if Utils.INT:
                    curtree.data = random.randint(Utils.MIN_VAL, Utils.MAX_VAL)
                else:
                    curtree.data = random.random()*(Utils.MAX_VAL - Utils.MIN_VAL) + Utils.MIN_VAL
            else:
                curtree.data = Utils.VAR

        x = linspace(1, 20, 1000)
        y = individual.tree.calculate(x)
        if isnan(y).any() or not isfinite(y).all():
            individual = Function(individual.points)



    @staticmethod
    def crossover(parent1, parent2):
        """Perform crossover with given parents."""

        tree1 = parent1.tree
        tree2 = parent2.tree

        depth = random.randint(1, Utils.MAX_DEPTH)

        chain1 = []
        chain2 = []
        chain1 = tree1.get_random_list(depth, chain1)
        chain2 = tree2.get_random_list(depth, chain2)

        exp1 = "parent1.tree.%s" % (".".join(chain1))
        exp2 = "parent2.tree.%s" % (".".join(chain2))
        # Worst code 2017
        exec("%s, %s = %s, %s" % (exp1, exp2, exp2, exp1))


    @staticmethod
    def makecopy(individual):
        """Return a copy of the individual."""
        raise AbstractMethodError

    def createLevel(self):
        if self.depth < Utils.MAX_DEPTH:
            lis = [random.choice(Utils.OPERATORS), Utils.MARKER, Utils.MARKER]
        else:
            lis = [random.choice(Utils.ARG_0), Utils.MARKER, Utils.MARKER]

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
                lis.insert(0, random.randint(Utils.MIN_VAL, Utils.MAX_VAL))
            else:
                lis.insert(0, random.random()*(Utils.MAX_VAL - Utils.MIN_VAL) + Utils.MIN_VAL)

        return lis


funkcja = Function()
print(funkcja.tree.traverse(funkcja.tree))

x = linspace(1, 200, 1000)
#print(x)
y = funkcja.tree.calculate(x)
plt.plot(x, y)
funkcja.mutate(funkcja)
y2 = funkcja.tree.calculate(x)
plt.plot(x, y2)
#print(funkcja.code)
print(funkcja.tree.traverse(funkcja.tree))
plt.show()