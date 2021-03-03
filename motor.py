import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.x = c.x
        self.amplitude = c.amplitudeFrontLeg
        self.frequency = c.frequencyFrontLeg
        self.phaseOffset = c.phaseOffsetFrontLeg
        self.motorValues = numpy.empty(1000)
        for i in range(1000):
            self.motorValues[i] = self.amplitude * \
                numpy.sin(self.frequency * self.x[i] + self.phaseOffset)

    def Set_Value(self, timeStep, robot):

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[timeStep],
            maxForce=c.maxForce)
