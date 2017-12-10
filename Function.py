from base import Individual
from base.Tree import Tree
from base import Utils
import random

AbstractMethodError = NotImplementedError("You must override this method")

class Function():
    """Represents an individual in a population"""
    tree = None
    code = []

    def __init__(self):
        """Construct a random individual."""
        self.tree = Tree()
        self.tree.createTree(self.code)

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
