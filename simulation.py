from robot import ROBOT
from world import WORLD

import pybullet as p
import time
import pybullet_data
import numpy
import pyrosim.pyrosim as pyrosim
import random
import math
import constants as c


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.directOrGUI = directOrGUI
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def __del__(self):
        p.disconnect()

    def run(self):
        for i in range(c.simulationSteps):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.directOrGUI == 'GUI':
                time.sleep(1 / 720)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def Get_Z_Coord(self):
        return self.robot.Get_Z_Coord()

    def Get_ID(self):
        return self.robot.Get_ID()