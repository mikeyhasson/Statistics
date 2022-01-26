from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import t
import numpy as np
import math
import seaborn as sns


def q2():
    prec_a =0.512
    n=1100
    var_p_hat = math.sqrt(prec_a*(1-prec_a)/n)
    alpha = 1- 0.95
    epsilon = (var_p_hat)*norm.ppf(1-alpha/2)
    revach_semach  = [prec_a -epsilon,prec_a+epsilon]
    print(revach_semach)

def q3():
    mu = 100
    sigma = 10
    grades =[96 ,82 ,112 ,107 ,99 ,96 ,93 ,108 ,110 ,123 ,117 ,104 ,102 ,105 ,113]
    mu_1_amp=np.mean(grades)
    sigma_1=sigma

    phsych_norm =norm(loc=mu_1_amp,scale=sigma_1)
    x=np.linspace(80,130,100)
    sns.histplot(data=grades,color='blue',stat='density',bins=np.arange(80,140,10))
    plt.plot(x,phsych_norm.pdf(x),color='black')
    plt.show()
    print("ampirical excpected value=",mu_1_amp)


    alpha = 1- 0.8
    n=len(grades)
    norm.ppf(1 - alpha / 2)
    epsilon =(sigma_1/math.sqrt(n)) * norm.ppf(1-alpha/2)
    revach_semach  = [mu_1_amp -epsilon,mu_1_amp+epsilon]
    print(revach_semach)

    alpha = 1- 0.95
    norm.ppf(1 - alpha / 2)
    epsilon =(sigma_1/math.sqrt(n)) * norm.ppf(1-alpha/2)
    revach_semach  = [mu_1_amp -epsilon,mu_1_amp+epsilon]
    print(revach_semach)

    sigma_amp = math.sqrt(np.var(grades))
    t_95 = t.ppf(1-alpha/2,df=n-1)
    epsilon = (sigma_amp/math.sqrt(n))*t_95
    revach_semach  = [mu_1_amp -epsilon,mu_1_amp+epsilon]
    print(revach_semach)

    alpha=1-0.9
    t_95 = t.ppf(1-alpha/2,df=n-1)
    epsilon = (sigma_amp/math.sqrt(n))*t_95
    revach_semach = [mu_1_amp -epsilon,mu_1_amp+epsilon]
    print(0.9,":",revach_semach)

    alpha=1-0.89
    t_95 = t.ppf(1-alpha/2,df=n-1)
    epsilon = (sigma_amp/math.sqrt(n))*t_95
    revach_semach = [mu_1_amp -epsilon,mu_1_amp+epsilon]
    print(0.89,":",revach_semach)
    

if __name__=="__main__":
    q2()
    q3()