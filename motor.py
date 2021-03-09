import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robot):

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce)
