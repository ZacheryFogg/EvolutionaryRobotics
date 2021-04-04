from solution import SOLUTION
from constants import numberOfGenerations
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate('GUI')
        for currGeneration in range(numberOfGenerations):
            print(currGeneration)
            self.Evolve_For_One_Generation()

        self.Show_Best()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # print(self.parent.weights)

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("\nParent Fitness : ", self.parent.fitness,
              " Child Fitness: ", self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate('GUI')
