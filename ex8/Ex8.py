from scipy.stats import norm
import numpy as np
import math


def q2():
    #Q2c
    alpha =norm.ppf(0.95)
    print(alpha)

    n=6
    mu = 7*math.sqrt(n)/math.sqrt(30)
    strength = 1-norm(loc=mu,scale=1).cdf(alpha)
    print(strength)

    #Q2d
    X  = [68.02,65.71,69.07,74.35,79.74,72.35]
    Z = (np.mean(X)-64.5)/math.sqrt(120/len(X))
    print(Z)

    #Q2e
    alpha=norm.ppf(0.05)
    print(alpha)
    mu *=-1
    strength = norm(loc=mu, scale=1).cdf(alpha)
    print(strength)
    Z = (np.mean(X)-78.5)/math.sqrt(120/len(X))
    print(Z)

def q3():
    #Q3b
    alpha = norm.ppf(0.95)
    print(alpha)

    #Q3e
    print(norm(loc=1.25,scale=math.sqrt(3)*5/8).cdf(alpha))

    #Q3f
    for n in range(0,1000,1):
        mu = 0.125 * math.sqrt(n)
        val=norm(loc=mu,scale=math.sqrt(3)*5/8).cdf(alpha)
        if val <=0.2:
            print(n,val)
            break





if __name__=="__main__":
    q2()
    q3()
