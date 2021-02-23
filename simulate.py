import pybullet as p
import time
import pybullet_data
import numpy
import pyrosim.pyrosim as pyrosim
import random
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

maxForce = 25

amplitudeF = numpy.pi/4
frequencyF = 10
phaseOffsetF = 0
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)
targetAnglesF = numpy.empty(1000)
for i in range(1000):
    targetAnglesF[i] = amplitudeF * numpy.sin(frequencyF * x[i] + phaseOffsetF)

amplitudeB = numpy.pi/4
frequencyB = 10
phaseOffsetB = 0
targetAnglesB = numpy.empty(1000)
for i in range(1000):
    targetAnglesB[i] = amplitudeB * numpy.sin(frequencyB * x[i] + phaseOffsetB)
# with open('./data/targetAnglesF.npy', 'wb') as f:
#     numpy.save(f, targetAnglesF)
# with open('./data/targetAnglesB.npy', 'wb') as f:
#     numpy.save(f, targetAnglesB)
# exit()
for i in range(1000):
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "BackLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_Back_Leg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesB[i],
        maxForce=maxForce)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_Front_Leg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesF[i],
        maxForce=maxForce)
    time.sleep(1 / 60)
with open('./data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)
with open('./data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)
p.disconnect()
