# plot average reward history

import re
import numpy as np
import pickle
import matplotlib.pyplot as plt

from plot_train_history import smoothing

if __name__ == '__main__':
    path = '/home/shugo/raisim_ws/raisimLib/raisimGymTorch/'
    filename1 = path + 'logfile_1.pkl'
    filename2 = path + 'logfile_2.pkl'

    with open(filename1, 'rb') as file:
        log1 = pickle.load(file)
        reward1 = log1['average ll performance']

    with open(filename2, 'rb') as file:
        log2 = pickle.load(file)
        reward2 = log2['average ll performance']

    reward = reward1 + reward2
    iterations = np.arange(0, len(reward))

    # average reward vs iterations
    plt.figure()
    plt.plot(iterations, reward, lw=2)
    plt.xlabel('Iterations (Epoch)')
    plt.ylabel('Avg. reward')

    # smoothing
    # reward_smooth = smoothing(reward, kernel_size=201)
    # plt.plot(iterations, reward_smooth)
    # plt.legend()

    plt.savefig('avg-reward.pdf', bbox_inches='tight')

    plt.show()
