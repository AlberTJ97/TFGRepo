from Genetic.Individual import Individual

class Population():
    SIZE = 0

    def __init__(self, lenght: int = 0):
        self.lenght = lenght
        self.individuals = [Individual(lenght = lenght) for _ in range(Population.SIZE)]