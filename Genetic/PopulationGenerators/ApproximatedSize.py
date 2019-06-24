from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Individual import *
from Genetic.PopulationGenerators import *
import random


class ApproximatedSize(PopulationGenerator):

    @staticmethod
    def generate_individuals(individual_type: BaseIndividual, chromosome_type: BaseChromosome,
                             list_of_gens_per_category: dict,  population_size: int, category_lenghts: dict,
                             percentage_of_features: int = -1) -> [BaseIndividual]:


        population: [BaseIndividual] = []

        for _ in range(population_size):
            selected_gens: [BaseGen] = []

            for category in category_lenghts:
                gens_per_category: int = category_lenghts[category] * percentage_of_features
                threshold = gens_per_category / category_lenghts[category]

                for index, _ in enumerate(list_of_gens_per_category[category]):
                    if random.uniform(0, 1) < threshold:
                        selected_gens.append(list_of_gens_per_category[category].pop(index))

            chromosome: BaseChromosome = chromosome_type(selected_gens, list(list_of_gens_per_category.values()))
            population.append(individual_type(chromosome))
            selected_gens.clear()

        return population