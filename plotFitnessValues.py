import numpy
import matplotlib.pyplot as plt

means1 = numpy.mean(numpy.load('Mutate1Neuron.npy'), axis=1)
std1 = numpy.std(numpy.load('Mutate1Neuron.npy'), axis=1)
means2 = numpy.mean(numpy.load('Mutate2Neuron.npy'), axis=1)
std2 = numpy.std(numpy.load('Mutate2Neuron.npy'), axis=1)
means3 = numpy.mean(numpy.load('Mutate3Neuron.npy'), axis=1)
std3 = numpy.std(numpy.load('Mutate3Neuron.npy'), axis=1)
means4 = numpy.mean(numpy.load('Mutate4Neuron.npy'), axis=1)
std4 = numpy.std(numpy.load('Mutate4Neuron.npy'), axis=1)
means5 = numpy.mean(numpy.load('Mutate5Neuron.npy'), axis=1)
std5 = numpy.std(numpy.load('Mutate5Neuron.npy'), axis=1)
means6 = numpy.mean(numpy.load('Mutate6Neuron.npy'), axis=1)
std6 = numpy.std(numpy.load('Mutate6Neuron.npy'), axis=1)
meansAll = numpy.mean(numpy.load('MutateAllNeuron.npy'), axis=1)
stdAll = numpy.std(numpy.load('MutateAllNeuron.npy'), axis=1)

plt.plot(means1, label='1 Random Neuron Mutated Mean', color='green')
plt.plot(means1 + std1,
         label='1 Random Neruon Mutated + Std',
         color='limegreen')
plt.plot(means1 - std1,
         label='1 Random Neruon Mutated - Std',
         color='darkgreen')
# plt.plot(means2, label='2 Random Neurons Mutated')
# plt.plot(means2 + std2, label='2 Random Neruons Mutated +Std')
# plt.plot(means2 - std2, label='2 Random Neruons Mutated -Std')
# plt.plot(means3, label='3 Random Neurons Mutated')
# plt.plot(means4, label='4 Random Neurons Mutated')
# plt.plot(means5, label='5 Random Neurons Mutated')
# plt.plot(means6, label='6 Random Neurons Mutated')
plt.plot(meansAll, label='All Neurons Mutated Mean', color='red')
plt.plot(meansAll + stdAll,
         label='All Neurons Mutated + Std',
         color='lightcoral')
plt.plot(meansAll - stdAll, label='All Neurons Mutated - Std', color='darkred')
plt.legend()
plt.xlabel('Generations')
plt.ylabel('Mean Fitness Value')
plt.title('Comparing Mean Generation Fitness with Different Mutation Rates')
plt.show()