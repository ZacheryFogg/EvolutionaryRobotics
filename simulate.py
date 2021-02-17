import pybullet as p
import time
import pybullet_data
import numpy
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


for i in range(1000):
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "BackLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    time.sleep(1 / 60)
with open('./data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)
with open('./data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)
p.disconnect()
