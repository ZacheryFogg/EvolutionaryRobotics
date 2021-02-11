import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
# width = 1
# length = 1
# height = 1
# x1 = 0
# y1 = 0
# z1 = .5

# x2 = 1
# y2 = 0
# z2 = 1.5
# pyrosim.Send_Cube(name="Box", pos=[x1, y1, z1], size=[length, width, height])
# pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2], size=[length, width, height])

towerX = 0
towerY = 0
towerZ = .5
towerDim = 1

for i in range(6):
    towerX = 0
    for j in range(6):
        towerZ = .5
        towerDim = 1
        for k in range(10):
            pyrosim.Send_Cube(name='Box', pos=[towerX, towerY, towerZ], size=[
                towerDim, towerDim, towerDim])
            towerZ += towerDim/2
            towerDim *= .9
            towerZ += towerDim / 2
        towerX += 1
    towerY += 1

pyrosim.End()
