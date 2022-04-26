import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import csv

def load_data(filename, step0=0):
    # read csv file with fieldname = [Wall time, Step, Value]

    steps = []
    values = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            steps.append(int(row['Step']) + step0)
            values.append(float(row['Value']))
    
    return steps, values


def smoothing(values, kernel_size):
    # return np.convolve(values, np.ones(kernel_size) / kernel_size, mode='same')
    return savgol_filter(values, window_length=kernel_size, polyorder=1)


def plot_loss_surrogate():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/'
    file1 = 'run-2022-04-18-15-49-19_Apr18_15-49-29-tag-PPO_surrogate.csv'
    file2 = 'run-2022-04-18-21-52-15_Apr18_21-52-20-tag-PPO_surrogate.csv'
    file3 = 'run-2022-04-19-14-31-43_Apr19_14-31-48-tag-PPO_surrogate.csv'

    steps1, values1 = load_data(path + file1)
    steps2, values2 = load_data(path + file2)
    steps3, values3 = load_data(path + file3)

    print(steps1[0], steps1[-1])

    # plot original data
    plt.figure()
    plt.plot(steps1, values1, '-b', steps2, values2, '.-g',steps3,values3, '--r', lw=0.5)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Loss surrogate')
    # plt.yscale('log')
    plt.legend(['adaptive w/ entropy','adaptive w/o entropy','fixed w/ entropy'])

    # smoothing data
    #values_smooth = smoothing(values, kernel_size=41)
    #plt.plot(steps, values_smooth, lw=2, label='smoothing')
    #plt.legend()

    #plt.ylim([-0.02, 0.05])

    plt.savefig('loss-surrogate.pdf', bbox_inches='tight')


def plot_loss_value_func():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/'
    file1 = 'run-2022-04-18-15-49-19_Apr18_15-49-29-tag-PPO_value_function.csv'
    file2 = 'run-2022-04-18-21-52-15_Apr18_21-52-20-tag-PPO_value_function.csv'
    file3 = 'run-2022-04-19-14-31-43_Apr19_14-31-48-tag-PPO_value_function.csv'

    steps1, values1 = load_data(path + file1)
    steps2, values2 = load_data(path + file2)
    steps3, values3 = load_data(path + file3)

    print(steps1[0], steps1[-1])

    # plot original data
    plt.figure()
    plt.plot(steps1, values1,'-b', steps2, values2, '.-g', steps3, values3, '--r', lw=0.5)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Loss value function')
    plt.yscale('log')
    plt.legend(['adaptive w/ entropy','adaptive w/o entropy','fixed w/ entropy'])

    # smoothing data
    #values_smooth = smoothing(values, kernel_size=41)
    #plt.plot(steps, values_smooth, lw=2, label='smoothing')
    #plt.legend()

    plt.savefig('loss-value-func.pdf', bbox_inches='tight')


def plot_policy_mean_noise_std():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/'
    file1 = 'run-2022-04-18-15-49-19_Apr18_15-49-29-tag-PPO_mean_noise_std.csv'
    file2 = 'run-2022-04-18-21-52-15_Apr18_21-52-20-tag-PPO_mean_noise_std.csv'
    file3 = 'run-2022-04-19-14-31-43_Apr19_14-31-48-tag-PPO_mean_noise_std.csv'

    steps1, values1 = load_data(path + file1)
    steps2, values2 = load_data(path + file2)
    steps3, values3 = load_data(path + file3)

    print(steps1[0], steps1[-1])

    # plot original data
    plt.figure()
    plt.plot(steps1, values1,'-b', steps2, values2, '.-g', steps3, values3, '--r', lw=2)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Policy mean noise std')
    # plt.yscale('log')
    plt.legend(['adaptive w/ entropy','adaptive w/o entropy','fixed w/ entropy'])

    # smoothing data
    # values_smooth = smoothing(values, kernel_size=21)
    # plt.plot(steps, values_smooth, lw=1.5, label='smoothing')
    # plt.legend()

    plt.savefig('policy-mean-noise-std.pdf', bbox_inches='tight')

def plot_learning_rate():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/'
    file1 = 'run-2022-04-18-15-49-19_Apr18_15-49-29-tag-PPO_learning_rate.csv'
    file2 = 'run-2022-04-18-21-52-15_Apr18_21-52-20-tag-PPO_learning_rate.csv'
    file3 = 'run-2022-04-19-14-31-43_Apr19_14-31-48-tag-PPO_learning_rate.csv'

    steps1, values1 = load_data(path + file1)
    steps2, values2 = load_data(path + file2)
    steps3, values3 = load_data(path + file3)

    print(steps1[0], steps1[-1])

    # plot original data
    plt.figure()
    plt.plot(steps1, values1,'-b', steps2, values2, '.-g', steps3, values3, '--r', lw=2)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Policy learning rate')
    # plt.yscale('log')
    plt.legend(['adaptive w/ entropy','adaptive w/o entropy','fixed w/ entropy'])

    # smoothing data
    # values_smooth = smoothing(values, kernel_size=21)
    # plt.plot(steps, values_smooth, lw=1.5, label='smoothing')
    # plt.legend()

    plt.savefig('policy-learning-rate.pdf', bbox_inches='tight')


if __name__ == '__main__':
    
    plot_loss_surrogate()
    plot_loss_value_func()
    plot_policy_mean_noise_std()
    plot_learning_rate()

    plt.show()
