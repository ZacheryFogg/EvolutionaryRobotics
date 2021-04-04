import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(3, 2)
        self.weights = (self.weights * 2) - 1

    def Evaluate(self, disp):
        # self.Create_Body()
        # self.Create_Brain()
        # self.Create_World()
        # # os.system("python simulate.py {}".format(disp))
        # os.system("start /B python simulate.py {} {}".format(disp, self.myID))
        # self.Start_Simulation(disp)
        # self.Wait_For_Simulation_To_End()
        pass

    def Start_Simulation(self, disp):
        self.Create_Body()
        self.Create_Brain()
        self.Create_World()
        # os.system("python simulate.py {}".format(disp))
        os.system("start /B python simulate.py {} {}".format(disp, self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = 'fitness{}.txt'.format(self.myID)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, 'r')
        self.fitness = float(f.read())
        f.close()
        print("\nFITNESS {} : {}\n".format(self.myID, self.fitness))
        cmd = 'rm {}'.format(fitnessFileName)
        os.system(cmd)

    def Create_Robot(self):
        pass

    def Set_ID(self, id):
        self.myID = id

    def Create_Body(self):
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

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back_Leg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front_Leg")

        sensorNeurons = [0, 1, 2]
        motorNeurons = [3, 4]
        for currCol in range(len(sensorNeurons)):
            for currRow in range(len(motorNeurons)):
                val = random.uniform(-1, 1)

                pyrosim.Send_Synapse(sourceNeuronName=currCol,
                                     targetNeuronName=currRow, weight=self.weights[currCol][currRow])

        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-.5)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-.5)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=.1)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=.1)
        pyrosim.End()

    def Create_World(self):
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

    def Mutate(self):
        col = random.randint(0, 2)
        row = random.randint(0, 1)
        self.weights[col, row] = random.random() * 2 - 1
