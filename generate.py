import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
width = 1
length = 1
height = 1
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])
pyrosim.End()
