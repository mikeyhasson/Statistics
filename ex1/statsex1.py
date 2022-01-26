from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def Empirical_F(x):#Q2a
    values, counts = np.unique(x, return_counts=True)
    sum_counts = np.copy(counts)
    for i in range(1, len(sum_counts)):
        sum_counts[i] = sum_counts[i] + sum_counts[i - 1]
    a = []
    for i in range(len(values)):
        for j in range(counts[i]):
            a.append([values[i], sum_counts[i] / len(x)])
    return np.array(a)


if __name__ == '__main__':

    x = binom.rvs(n=5, p=1 / 6, size=20)
    print(x)#Q2b
    a = Empirical_F(x)
    print(a)#Q2c
    plt.step(a[:, 0], a[:, 1], where='post')
    plt.ylim(0, 1)
    plt.show()#Q2d


    Y=[i for i in range(6)]
    Y_prob = binom.cdf(Y, 5, 1/6)
    print(Y_prob)#Q2e

    plt.step(a[:, 0], a[:, 1], where='post')
    plt.plot(Y, Y_prob)
    plt.ylim(0, 1)
    plt.show()#Q2f

    # Q2g
    for k in [100,200,1000]:
        x = binom.rvs(n=5, p=1 / 6, size=k)
        print(x)
        a = Empirical_F(x)
        plt.plot(a[:, 0], a[:, 1])
        plt.ylim(0, 1)
        plt.show()



