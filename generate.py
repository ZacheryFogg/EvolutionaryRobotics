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
    width = 1
    length = 1
    height = 1
    x = 0
    y = 0
    z = .5
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[
                      length, width, height])
    pyrosim.End()


Create_World()
Create_Robot()
