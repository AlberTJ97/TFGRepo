from EmailParser import DataCategory
from Log.LoggerHandler import LoggerHandler
from Genetic.Fitness import TFIDF
from Genetic.Operations import Mutation, Crossover
from Genetic.Components import Population, Individual

class SimpleGASpecification:

    def __init__(self, train_data: DataCategory, test_data: DataCategory, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0, fitness_penalization: float = 0.0,
                 cutting_points: int = 0, gt_max_features: float = 0.0):

        Population.setMaxPopulationSize(populationSize)
        Individual.setMaxIndividualFeatures(maxIndividualFeatures)
        TFIDF.PENALIZATION_BAD_CATEGORY = fitness_penalization
        TFIDF.PENALIZATION_GT_MAX_FEATURES = gt_max_features
        Mutation.MUTATION_RATE = mutation_rate
        Crossover.CUTTING_POINTS = cutting_points

        self.train_data: list[DataCategory] = train_data
        self.test_data: list[DataCategory] = test_data
        self.population: list[Population] = []

        for category_data in train_data:
            self.population.append(Population(category_data.corpus))
            LoggerHandler.log(__name__, f"Population for category_data '{category_data.name}' has been initialized.")
