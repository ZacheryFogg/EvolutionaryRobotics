import sys
from simulation import SIMULATION
import os
# import pybullet as p
# import time
# import pybullet_data
# import numpy
# import pyrosim.pyrosim as pyrosim
# import random
# import math
# import constants as c

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0, 0, -9.8)
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate("body.urdf")
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)

# for i in range(c.simulationSteps):
#     p.stepSimulation()
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
#         "BackLeg")
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
#         "FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robot,
#         jointName="Torso_Back_Leg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=c.targetAnglesBackLeg[i],
#         maxForce=c.maxForce)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robot,
#         jointName="Torso_Front_Leg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=c.targetAnglesFrontLeg[i],
#         maxForce=c.maxForce)
#     time.sleep(1 / 60)
# with open('./data/backLegSensorValues.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues)
# with open('./data/frontLegSensorValues.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues)
# p.disconnect()
directOrGUI = 'GUI'
if len(sys.argv) > 1:
    directOrGUI = sys.argv[1]
if len(sys.argv) > 2:
    solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()

# Check if z if less than 3, then rewrite fitness to 100
z = simulation.Get_Z_Coord()
# print('\n\n Z Coord: ', z)
if (z <= 2.4):

    f = open("tmp{}.txt".format(simulation.Get_ID()), 'w')
    f.write('100')
    f.close()
    os.rename("tmp" + str(simulation.Get_ID()) + ".txt",
              "fitness" + str(simulation.Get_ID()) + ".txt")
else:
    simulation.Get_Fitness()