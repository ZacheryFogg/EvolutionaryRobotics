import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import constants as c
import os
import time


class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
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
        # print("\nFITNESS {} : {}\n".format(self.myID, self.fitness))
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
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",
                          pos=[0, 0, 1],
                          size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg",
                           parent="Torso",
                           child="FrontLeg",
                           type="revolute",
                           position="0 .5 1.0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[0.2, 1, .2])
        pyrosim.Send_Joint(name="Torso_BackLeg",
                           parent="Torso",
                           child="BackLeg",
                           type="revolute",
                           position="0 -.5 1.0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[.2, 1, .2])
        # Left Leg
        pyrosim.Send_Joint(name="Torso_LeftLeg",
                           parent="Torso",
                           child="LeftLeg",
                           type="revolute",
                           position="-.5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LeftLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])
        # Right Leg
        pyrosim.Send_Joint(name="Torso_RightLeg",
                           parent="Torso",
                           child="RightLeg",
                           type="revolute",
                           position=".5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name='RightLeg', pos=[.5, 0, 0], size=[1, .2, .2])
        # Lower Front
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg",
                           parent="FrontLeg",
                           child="FrontLowerLeg",
                           type="revolute",
                           position="0 1 0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg",
                          pos=[0, 0, -.5],
                          size=[0.2, .2, 1])
        # Back Lower Leg
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg",
                           parent="BackLeg",
                           child="BackLowerLeg",
                           type="revolute",
                           position="0 -1 0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg",
                          pos=[0, 0, -.5],
                          size=[.2, .2, 1])
        # Right Lower Leg
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg",
                           parent="RightLeg",
                           child="RightLowerLeg",
                           type="revolute",
                           position="1 0 0",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name='RightLowerLeg',
                          pos=[0, 0, -.5],
                          size=[.2, .2, 1])

        # Left Lower Leg
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg",
                           parent="LeftLeg",
                           child="LeftLowerLeg",
                           type="revolute",
                           position="-1 0 0",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LeftLowerLeg',
                          pos=[0, 0, -.5],
                          size=[.2, .2, 1])
        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName='LeftLeg')
        pyrosim.Send_Sensor_Neuron(name=4, linkName='RightLeg')
        pyrosim.Send_Sensor_Neuron(name=5, linkName='FrontLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=6, linkName='BackLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=7, linkName='RightLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=8, linkName='LeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_LeftLeg')
        pyrosim.Send_Motor_Neuron(name=12, jointName='Torso_RightLeg')
        pyrosim.Send_Motor_Neuron(name=13, jointName='FrontLeg_FrontLowerLeg')
        pyrosim.Send_Motor_Neuron(name=14, jointName='BackLeg_BackLowerLeg')
        pyrosim.Send_Motor_Neuron(name=15, jointName='RightLeg_RightLowerLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='LeftLeg_LeftLowerLeg')

        for currCol in range(c.numSensorNeurons):
            for currRow in range(c.numMotorNeurons):
                val = random.uniform(-1, 1)

                pyrosim.Send_Synapse(sourceNeuronName=currCol,
                                     targetNeuronName=currRow +
                                     c.numSensorNeurons,
                                     weight=self.weights[currCol][currRow])

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
        pyrosim.Send_Cube(name="Box",
                          pos=[x, y, z],
                          size=[length, width, height])
        pyrosim.End()

    def Mutate(self):
        col = random.randint(0, c.numSensorNeurons - 1)
        row = random.randint(0, c.numMotorNeurons - 1)
        self.weights[col, row] = random.random() * 2 - 1
