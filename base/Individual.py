AbstractMethodError = NotImplementedError("You must override this method")


class Individual:
    """Represents an individual in a population"""
    def __init__(self):
        """Construct a random individual."""
        raise AbstractMethodError

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
