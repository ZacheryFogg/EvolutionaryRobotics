from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
import pybullet as p
import os
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        # self.motors = {}
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        cmd = 'rm brain{}.nndf'.format(self.solutionID)
        os.system(cmd)

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timeStep):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(timeStep)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            # print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, timeStep):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(
                    neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        # stateOfLinkZero = p.getLinkState(self.robot, 0)
        basePositionAndOrientation = p.getBasePositionAndOrientation(
            self.robot)
        # positionOfLinkZero = stateOfLinkZero[0]
        basePosition = basePositionAndOrientation[0]
        # xCoordinateOfLinkZero = positionOfLinkZero[0]
        xPosition = basePosition[0]
        zPosition = basePosition[2]

        f = open("tmp{}.txt".format(self.solutionID), 'w')
        # f.write(str(xCoordinateOfLinkZero))
        f.write(str(xPosition))
        f.close()

        # cmd = 'rename tmp{}.txt fitness{}.txt'.format(
        #     self.solutionID, self.solutionID)
        # os.system(cmd)
        os.rename("tmp" + str(self.solutionID) + ".txt",
                  "fitness" + str(self.solutionID) + ".txt")
        # cmd = 'rm tmp{}.txt'.format(self.solutionID)
        # os.system(cmd)
