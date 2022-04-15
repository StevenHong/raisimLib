import re
import numpy as np
import matplotlib.pyplot as plt
from array import array

path = '/home/roahm/'
filename = path + 'output.log'

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

reward = []

content = open(filename).read()
res = re.finditer("(average ll reward).+[-0.123456789]+", content, re.M)
for line in res:
    num = re.search("[-0.123456789]+", line[0])
    reward.append(float(num[0]))


iterations = np.arange(0, len(reward))

# plot the reward vs iterations
plt.figure()
plt.plot(iterations, reward, lw=2)
plt.xlabel('Iterations (Epoch)')
plt.ylabel('Avg. Reward')

plt.savefig('avg-reward.pdf', bbox_inches='tight')
plt.show()
