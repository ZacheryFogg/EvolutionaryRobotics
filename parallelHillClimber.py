from solution import SOLUTION
from constants import numberOfGenerations
from constants import populationSize
import copy
import os
import numpy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        self.parents = {}
        self.timestep = 0
        self.nextAvailableID = 0
        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        # print(self.parents)
        self.agent_fitnesses = numpy.zeros(
            (numberOfGenerations, populationSize))
        print(self.agent_fitnesses.shape)
        # print(self.agent_fitnesses)

    def Evolve(self):
        # for key in self.parents:
        #     parent = self.parents[key]

        #     # parent.Evaluate('GUI')
        #     parent.Start_Simulation('DIRECT')

        # for key in self.parents:

        #     parent = self.parents[key]
        #     parent.Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)

        for currGeneration in range(numberOfGenerations):

            self.Evolve_For_One_Generation()
            # print('\n\nCURRENT GENERATION: {}\n\n'.format(currGeneration))
            # Record fitness values. We don't care about the first generation as they did not mutate
            for key in self.parents:
                # if key == populationSize:
                #     print("LENGTH OF PARENTS: {}".format(len(self.parents)))
                #     key -= 1
                if self.parents[key].fitness == 100:
                    self.parents[key].fitness = 0
                # print('FITNESS {} KEY {}'.format(self.parents[key].fitness,
                #                                  key))
                self.agent_fitnesses[currGeneration,
                                     key] = self.parents[key].fitness
            # print('Increment gen')
        print(self.agent_fitnesses)
        numpy.save('MutateAllNeuron', self.agent_fitnesses)
        self.Show_Best()

    def Evaluate(self, solutions, disp='DIRECT'):
        for key in solutions:
            solutions[key].Start_Simulation(disp)

            # parent.Evaluate('GUI')
            # parent.Start_Simulation('DIRECT')

        for key in solutions:

            solutions[key].Wait_For_Simulation_To_End()
            # parent.Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)

        self.Print()
        self.Select()
        pass

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        # self.child = copy.deepcopy(self.parent)
        # for key in self.children:
        #     print(self.children[key])
        # exit()

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()
            # self.child.Mutate()
        # print(self.parent.weights)

    def Select(self):
        print('Step: ', self.timestep)
        self.timestep += 1
        for key in self.parents:
            # write out fitness valuess
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

        # if self.parent.fitness > self.child.fitness:
        #     self.parent = self.child

    def Print(self):
        print('\n\n')
        # print('write fitness at gen {}'.format(self.curr_gen))
        for key in self.parents:
            print('\n Parent Fitness: {} Child Fitness: {}\n'.format(
                self.parents[key].fitness, self.children[key].fitness))
        print('\n\n')

    def Show_Best(self):
        bestFittness = 10000
        for key in self.parents:
            if self.parents[key].fitness < bestFittness:
                bestKey = key
                bestFittness = self.parents[key].fitness
        print('Lowest Fitness: {}'.format(bestFittness))
        self.parents[bestKey].Start_Simulation('GUI')
