import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from itertools import product


def b_and_c (t):
    n=100000
    X_random = [np.mean(np.random.choice(np.arange(1,7),size=t,p=[1/6]*6)) for i in range(n)]
    sns.kdeplot(data=X_random)
    mean_X_rand = np.average(X_random)
    print("mean val of amperial is", mean_X_rand)
    sd_X_rand = math.sqrt(np.sum(np.power(X_random - mean_X_rand,2))/n)
    print("standard deviation of amperial is", sd_X_rand)
    plt.show()


if __name__ == "__main__":
    b_and_c(15)


    X=np.arange(1,7)
    Probs_X = [1/6]*6
    d={'val':X, 'probs':Probs_X}
    df = pd.DataFrame(data=d)
    print("Q4a:")
    print("Table of X probs:",df.to_string(index=False))
    mean_val = np.sum(X*Probs_X)
    print("Expected val of X:",mean_val)

    sd = math.sqrt(np.sum(np.power(X - mean_val,2))/np.size(X))
    print ("standard deviation of X:",sd)

    all_possible = np.array([(i+j)/2.0 for j in range(1,7) for i in range(1,7)])
    X_2, Probs_X_2 = np.unique(all_possible, return_counts=True)
    Probs_X_2=Probs_X_2/np.size(all_possible)
    mean_val_X_2 = np.sum(X_2*Probs_X_2)
    print("Expected val of X_2:",mean_val_X_2)

    sd_X_2 = math.sqrt(np.sum(np.power(all_possible - mean_val_X_2,2))/np.size(all_possible))
    print ("standard deviation of X_2:",sd_X_2)
    #Q4b
    n=100000
    X_2_random = np.random.choice(X_2,size=n,p=Probs_X_2)

    #sns.kdeplot(data=X_2_random)
    #plt.show()

    print("Q4c:")
    mean_X_2_rand = np.average(X_2_random)
    print("mean val is", mean_X_2_rand)
    sd_X_2_rand = math.sqrt(np.sum(np.power(X_2_random - mean_X_2_rand,2))/n)
    print("standard deviation is", sd_X_2_rand)

    #Q4d
    x = np.linspace(mean_val_X_2 - 3*sd_X_2, mean_val_X_2 + 3*sd_X_2, 100)
    plt.plot(x, norm.pdf(x, mean_val_X_2, sd_X_2))
    sns.kdeplot(data=X_2_random)
    plt.show()

    print("Q4e:")
    #b_and_c(3)
    #b_and_c(6)
    #b_and_c(8)
    b_and_c(10)
    b_and_c(15)

    n=15
    print("Question 4f:", norm.ppf([0.95], loc=mean_val, scale=sd/math.sqrt(n)))
