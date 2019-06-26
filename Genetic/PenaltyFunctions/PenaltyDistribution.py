from Genetic.PenaltyFunctions import *
from Genetic.Individual import *
from Genetic.Chromosome import  *
import numpy as np

class PenaltyDistribution(PenaltyFunctions):

    @staticmethod
    def penalize(individual: BaseIndividual):
        distribution_diff: list = individual.chromosome.distance_from_ideal()
        ideal_distribution: list = list(BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION.values())
        deviation_percentage: list = np.divide(distribution_diff, ideal_distribution)


        penalization_per_category: list = []
        for value in deviation_percentage:
            penalization_per_category.append(value)

        individual.score = individual.score - (sum(penalization_per_category) * PenaltyDistribution.RATE)