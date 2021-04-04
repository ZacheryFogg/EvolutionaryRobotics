import numpy

populationSize = 2
numberOfGenerations = 2
maxForce = 25
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)
simulationSteps = 1000
# Variables controling Front leg
amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0
targetAnglesFrontLeg = numpy.empty(1000)
for i in range(1000):
    targetAnglesFrontLeg[i] = amplitudeFrontLeg * \
        numpy.sin(frequencyFrontLeg * x[i] + phaseOffsetFrontLeg)

# Variable Controling Back Leg
amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0
targetAnglesBackLeg = numpy.empty(1000)
for i in range(1000):
    targetAnglesBackLeg[i] = amplitudeBackLeg * \
        numpy.sin(frequencyBackLeg * x[i] + phaseOffsetBackLeg)

# with open('./data/targetAnglesF.npy', 'wb') as f:
#     numpy.save(f, targetAnglesF)
# with open('./data/targetAnglesB.npy', 'wb') as f:
#     numpy.save(f, targetAnglesB)
# exit()
