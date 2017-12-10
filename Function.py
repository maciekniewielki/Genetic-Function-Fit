from base import Individual
from base import Tree
from base import Utils

AbstractMethodError = NotImplementedError("You must override this method")

class Function(Individual):
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
        raise AbstractMethodError

    @staticmethod
    def makecopy(individual):
        """Return a copy of the individual."""
        raise AbstractMethodError
