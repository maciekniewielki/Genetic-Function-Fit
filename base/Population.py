from random import random, randrange
import Utils


class Population:
    """Represents a population of individuals."""
    def __init__(self, size, IndividualClass, *args):
        """Construct a population with a given size."""
        self.size = size
        self.individuals = [IndividualClass(*args) for _ in range(size)]
        self.crossover_prob = 0.7
        self.mutation_prob = 3e-3
        self.IndividualClass = IndividualClass

    def advance_step(self):
        """Performs selection, crossover and mutation over the population and returns the maximum fitness."""
        self.apply_selection()
        self.apply_crossover()
        self.apply_mutation()
        self.sort_by_fitness()
        return self.individuals[0]

    def apply_selection(self, selection_type="roulette"):
        """Apply the given selection operator for the current population."""
        if selection_type == "roulette":
            self._roulette()
        elif selection_type == "tournament":
            self._tournament()
        else:
            raise Utils.InvalidParameterError("Wrong parameter. No option for %s" % selection_type)

    def apply_crossover(self):
        """Apply the crossover operator"""
        for _ in range(self.size):
            parent1, parent2 = self.get_random(), self.get_random()
            if random() > self.crossover_prob or parent1 == parent2:
                continue
            self.IndividualClass.crossover(parent1, parent2)

    def apply_mutation(self):
        """Apply the mutation operator."""
        for ii in range(self.size):
            if random.random() < self.mutation_prob:
                self.IndividualClass.mutate(self.individuals[ii])

    def _tournament(self):
        """Apply tournament selection operator."""
        new_population = []
        while len(new_population) < self.size:
            warriors = [self.get_random() for _ in range(6)]
            winner = max(warriors, key=lambda ii: self.IndividualClass.get_fitness(ii))
            new_population.append(self.IndividualClass.makecopy(winner))

        self.individuals = new_population

    def _roulette(self):
        """Apply roulette selection operator."""
        fitnesses = [self.IndividualClass.get_fitness(ii) for ii in self.individuals]

        fitness_sum = sum(fitnesses)
        new_population = []
        while len(new_population) < self.size:
            temp_sum = 0
            rand = random()
            for ii in self.individuals:
                temp_sum += self.IndividualClass.get_fitness(ii) / fitness_sum
                if temp_sum >= rand:
                    new_population.append(self.IndividualClass.makecopy(ii))
                    break

        self.individuals = new_population

    def sort_by_fitness(self):
        """Sort the current population based on fitness function. Best individuals are first."""
        self.individuals = sorted(self.individuals, key=lambda ii: self.IndividualClass.get_fitness(ii), reverse=True)

    def get_random(self):
        """Returns a random individual from the population."""
        index = randrange(self.size)
        return self.individuals[index]
