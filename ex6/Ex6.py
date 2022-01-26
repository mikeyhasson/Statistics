from scipy.stats import poisson
from scipy.stats import expon
import numpy as np

for la in {0.1,10}:
    poisson_new = poisson (la)
    expon_new = expon (scale = 1/la)

    x_all = np.array([np.mean(expon_new.rvs(size=20)) for i in range(10000)])
    x_all = 1/x_all
    var = np.var(x_all)
    expected = np.mean(x_all)
    MSE_x = var + (expected - la)**2
    print("lambda:",la,"MSE_1:",MSE_x)

    x_all = np.array([np.mean(poisson_new.rvs(size=20)) for i in range(10000)])
    var = np.var(x_all)
    expected = np.mean(x_all)
    MSE_x = var + (expected - la)**2
    print("lambda:",la,"MSE_2:",MSE_x)

