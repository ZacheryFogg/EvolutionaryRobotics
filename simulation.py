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
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def run(self):
        for i in range(c.simulationSteps):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1 / 60)
