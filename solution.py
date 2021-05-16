import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c


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
        while True:
            try:
                f = open(fitnessFileName, 'r')
                break
            except:
                print('Fitness File Error')
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
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 1

        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")
        width = 1
        length = 1
        height = 1
        x = 1.5
        y = 0
        z = 1.5
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso",
                          pos=[0, 0, 3],
                          size=[length, width, height])
        # Front Leg
        pyrosim.Send_Joint(name="Torso_FrontLeg",
                           parent="Torso",
                           child="FrontLeg",
                           type="revolute",
                           position="0 .5 3.0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[0.2, 1, .2])
        # Back Leg
        pyrosim.Send_Joint(name="Torso_BackLeg",
                           parent="Torso",
                           child="BackLeg",
                           type="revolute",
                           position="0 -.5 3.0",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[.2, 1, .2])
        # Left Leg
        pyrosim.Send_Joint(name="Torso_LeftLeg",
                           parent="Torso",
                           child="LeftLeg",
                           type="revolute",
                           position="-.5 0 3.0",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name='LeftLeg', pos=[-0.5, 0, 0], size=[1, .2, .2])
        # Right Leg
        pyrosim.Send_Joint(name="Torso_RightLeg",
                           parent="Torso",
                           child="RightLeg",
                           type="revolute",
                           position=".5 0 3.0",
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

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName='LeftLeg')
        # pyrosim.Send_Sensor_Neuron(name=4, linkName='RightLeg')
        pyrosim.Send_Sensor_Neuron(name=0, linkName='FrontLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=2, linkName='RightLowerLeg')
        pyrosim.Send_Sensor_Neuron(name=3, linkName='LeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName='Torso_LeftLeg')
        pyrosim.Send_Motor_Neuron(name=7, jointName='Torso_RightLeg')
        pyrosim.Send_Motor_Neuron(name=8, jointName='FrontLeg_FrontLowerLeg')
        pyrosim.Send_Motor_Neuron(name=9, jointName='BackLeg_BackLowerLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='RightLeg_RightLowerLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='LeftLeg_LeftLowerLeg')

        for currCol in range(c.numSensorNeurons):
            for currRow in range(c.numMotorNeurons):
                val = random.uniform(-1, 1)

                pyrosim.Send_Synapse(sourceNeuronName=currCol,
                                     targetNeuronName=currRow +
                                     c.numSensorNeurons,
                                     weight=self.weights[currCol][currRow])
        pyrosim.End()

    def Create_Maze(self):

        # Send rectangles that represent walls
        # pyrosim.Send_Cube(name="Wall1", pos=[-2, -3, 1], size=[10, 2, 2])

        # pyrosim.Send_Cube(name="Wall4", pos=[-8, .25, 1], size=[2, 8.5, 2])
        # pyrosim.Send_Cube(name="Wall5", pos=[-1, 6.25, 1], size=[2, 7.5, 2])
        # pyrosim.Send_Cube(name="Wall6", pos=[-8, 11, 1], size=[16, 2, 2])
        pyrosim.Send_Cube(name="Wall1", pos=[.5, 3.5, 1], size=[7, 2, 2])
        pyrosim.Send_Cube(name="Wall2", pos=[3, -4, 1], size=[2, 12, 2])
        pyrosim.Send_Cube(name="Wall3", pos=[-3, -.5, 1], size=[2, 3, 2])
        pyrosim.Send_Cube(name="Wall4", pos=[-6, -8.5, 1], size=[14, 2, 2])

    def Create_Block_Field(self):

        for x in range(-10, 5, 2):
            for y in range(-5, 10, 2):
                if not (x == 0 and y == 0):

                    pyrosim.Send_Cube(name="Box{}_{}".format(x, y),
                                      pos=[x, y, 1],
                                      size=[1.4, 1.4, 2])

    def Create_Runway(self):

        pyrosim.Send_Cube(name="Platform", pos=[-7, 0, 1], size=[30, 4.2, 2])

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        width = 1
        length = 1
        height = 1
        x = -3
        y = 3
        z = .5

        # self.Create_Block_Field()
        # self.Create_Maze()
        self.Create_Runway()

        pyrosim.End()

    def Mutate(self):
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        # col = random.randint(0, c.numSensorNeurons - 1)
        # row = random.randint(0, c.numMotorNeurons - 1)
        # self.weights[col, row] = random.random() * 2 - 1
        for col in range(c.numSensorNeurons):
            for row in range(c.numMotorNeurons):
                self.weights[col, row] = random.random() * 2 - 1
