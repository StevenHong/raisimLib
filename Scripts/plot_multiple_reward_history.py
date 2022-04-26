import re
import numpy as np
import matplotlib.pyplot as plt
from array import array

path = '/home/roahm/'
filename1 = path + 'training_1.log'
filename3 = path + 'training_3.log'

#reward = array('f')

#with open(filename) as f:
#    for line in f:
#        if (re.search("average ll reward", line)):
#        	result = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", line)
#        	print(float(result[0]))
#        	reward.append(float(result[0]))

#with open(filename) as f:
#  for line in f:
#    if re.match("^(average ll reward).*$", line):
#      res = re.search("[-0.123456789]+", line)
#      reward.append(float(res[0]))

reward1 = []
reward3 = []

content1 = open(filename1).read()
res1 = re.finditer("(average ll reward).+[-0.123456789]+", content1, re.M)
for line in res1:
    num = re.search("[-0.123456789]+", line[0])
    reward1.append(float(num[0]))

content3 = open(filename3).read()
res3 = re.finditer("(average ll reward).+[-0.123456789]+", content3, re.M)
for line in res3:
    num = re.search("[-0.123456789]+", line[0])
    reward3.append(float(num[0]))

iterations1 = np.arange(0, len(reward1))
iterations3 = np.arange(0, len(reward3))

# plot the reward vs iterations
plt.figure()
plt.plot(iterations1, reward1, '-b', iterations3, reward3, '--r', lw=2)
plt.xlabel('Iterations (Epoch)')
plt.ylabel('Avg. Reward')
plt.legend(['Adaptive Learning Rate','Fixed Learning Rate'])

plt.savefig('avg-reward.pdf', bbox_inches='tight')
plt.show()
