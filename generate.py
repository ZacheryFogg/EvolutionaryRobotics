import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    width = 1
    length = 1
    height = 1
    x = -3
    y = 3
    z = .5
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[
                      length, width, height])
    pyrosim.End()


def Create_Robot():
    pass


def Generate_Body():
    width = 1
    length = 1
    height = 1
    x = 1.5
    y = 0
    z = 1.5
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[
                      length, width, height])
    pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso",
                       child="FrontLeg", type="revolute", position="2 0 1.0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, y, -.5], size=[
                      length, width, height])
    pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso",
                       child="BackLeg", type="revolute", position="1 0 1.0")
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, y, -.5], size=[
                      length, width, height])

    pyrosim.End()


def Generate_Brain():

    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back_Leg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front_Leg")
    pyrosim.End()


Generate_Body()
Generate_Brain()
Create_World()
Create_Robot()
