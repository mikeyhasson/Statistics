from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import gamma
from scipy.stats import t
import numpy as np
import math

def q2():
    #Q2b
    n=10
    mu_0 =70

    print("Q2b:", t(n-1).ppf(0.95))

    X=[67 ,72 ,79, 71, 66 ,77, 78, 74, 75, 64]
    var_X = np.var(X,ddof=1)
    T_X=(np.mean(X)-mu_0)/math.sqrt(var_X/len(X))
    print("Q2c:T(X)=", T_X)
    print("Q2c:min level=", 1-t(n-1).cdf(T_X))

    print("Q2d: rejection=", norm.ppf(1-0.05))

    sigma=4
    Z_X=(np.mean(X)-mu_0)/(sigma/math.sqrt(len(X)))
    print("Q2e:Z(X)=", Z_X)
    min_level=1-norm.cdf(Z_X)
    print("Q2e:min level=", min_level)

    #Q2f:
    print("Q2f:Pr for Q2d=", norm(scale=2/(sigma/math.sqrt(n))).cdf(min_level))
    print("Q2f:Pr for Q2b=", t(n-1).cdf(1.833))









def q3():
    #Q3b
    alpha =0.05

    lambda_0 = 0.2
    lambda_A=0.6
    n =30

    #poisson to normal
    print("Q3b, poisson-to-normal",norm.ppf(1-alpha))

    #sum of poissons
    poisson_lambda = n*lambda_0
    print("Q3b, sum of poissons",poisson(poisson_lambda).ppf(1-alpha))
    print("Probability that the sum is >= 10 is:",1-poisson(poisson_lambda).cdf(9))
    print("Probability that the sum is >= 11 is:",1-poisson(poisson_lambda).cdf(10))


    #Q3d
    lambda_0 = 0.2
    n = 30

    # poisson to normal
    print("Q3d, exp-to-normal", norm.ppf(alpha))

    # sum of poissons
    Q3d = gamma(a=n,scale=1/lambda_0).ppf(alpha)
    print("Q3d, sum of exps", Q3d)

    #Q3e
    calc =( (1/n)*Q3d-(1/lambda_0))*(lambda_0*math.sqrt(n))
    print("Q3e:",calc)

    #Q3f
    print("Q3f, A:", gamma(a=n,scale=1/lambda_A).cdf(Q3d))
    print("Q3f, B:", 1-poisson(n*lambda_A).cdf(10))



if __name__=="__main__":
    q2()
    q3()
