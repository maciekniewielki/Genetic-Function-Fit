from Individual import Individual
from random import random
import Utils


class Population:
    """Represents a population of individuals."""
    def __init__(self, size):
        """Construct a population with a given size."""
        self.size = size
        self.individuals = [Individual() for _ in range(size)]
        raise NotImplementedError("Not yet implemented")

    def apply_selection(self, selection_type="roulette"):
        """Apply the given selection operator for the current population."""
        if selection_type == "roulette":
            self._roulette()
        else:
            raise Utils.InvalidParameterError("Wrong parameter. No option for %s" % selection_type)

    def _roulette(self):
        """Apply roulette selection operator."""
        fitness_sum = sum([Individual.get_fitness(ii) for ii in self.individuals])
        new_population = []
        while len(new_population) < self.size:
            temp_sum = 0
            rand = random()
            for ii in self.individuals:
                temp_sum += Individual.get_fitness(ii) / fitness_sum
                if temp_sum >= rand:
                    new_population.append(ii)
        self.individuals = new_population

    def sort_by_fitness(self):
        """Sort the current population based on fitness function. Best individuals are first."""
        self.individuals = sorted(self.individuals, key=lambda ii: Individual.get_fitness(ii))
