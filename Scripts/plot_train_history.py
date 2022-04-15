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

    path = '/home/roahm/Downloads/'
    file1 = 'run-2022-03-07-13-17-11_Mar07_13-17-12-tag-Loss_surrogate.csv'

    steps, values = load_data(path + file1)

    print(steps[0], steps[-1])

    # plot original data
    plt.figure()
    plt.plot(steps, values, lw=0.5)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Loss surrogate')
    # plt.yscale('log')

    # smoothing data
    values_smooth = smoothing(values, kernel_size=41)
    plt.plot(steps, values_smooth, lw=2, label='smoothing')
    plt.legend()

    plt.ylim([-0.02, 0.05])

    plt.savefig('loss-surrogate.pdf', bbox_inches='tight')


def plot_loss_value_func():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/Downloads/'
    file1 = 'run-2022-03-07-13-17-11_Mar07_13-17-12-tag-Loss_value_function.csv'

    steps, values = load_data(path + file1)

    print(steps[0], steps[-1])

    # plot original data
    plt.figure()
    plt.plot(steps, values, lw=0.5)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Loss value function')
    plt.yscale('log')

    # smoothing data
    values_smooth = smoothing(values, kernel_size=41)
    plt.plot(steps, values_smooth, lw=2, label='smoothing')
    plt.legend()

    plt.savefig('loss-value-func.pdf', bbox_inches='tight')


def plot_policy_mean_noise_std():
    # read two log files. I restarted run2 after run1.

    path = '/home/roahm/Downloads/'
    file1 = 'run-2022-03-07-13-17-11_Mar07_13-17-12-tag-Policy_mean_noise_std.csv'

    steps, values = load_data(path + file1)

    print(steps[0], steps[-1])

    # plot original data
    plt.figure()
    plt.plot(steps, values, lw=2)
    plt.xlabel('Iteration (Epoch)')
    plt.ylabel('Policy mean noise std')
    # plt.yscale('log')

    # smoothing data
    # values_smooth = smoothing(values, kernel_size=21)
    # plt.plot(steps, values_smooth, lw=1.5, label='smoothing')
    # plt.legend()

    plt.savefig('policy-mean-noise-std.pdf', bbox_inches='tight')


if __name__ == '__main__':
    
    plot_loss_surrogate()
    plot_loss_value_func()
    plot_policy_mean_noise_std()

    plt.show()
