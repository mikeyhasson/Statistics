import numpy as np
import matplotlib.pyplot as plt

n=10
mu = np.arange(50,71,0.2)
mu_1 = np.power(60-mu,2)
mu_2 = np.full_like(mu,25.0/n)
mu_3 = (25*n + 4*np.power(60-mu,2))/pow(n+2,2)

plt.plot(mu,mu_1,label = "mu1")
plt.plot(mu,mu_2,label = "mu2")
plt.plot(mu,mu_3,label = "mu3")
plt.legend()
plt.ylim([0,10])
plt.ylabel("MSE")
plt.xlabel("mu")
plt.show()

grades = np.array([81,95,85,75,98,100,85,86,92,91])
mu_1 = 60
mu_2 = np.mean(grades)
mu_3 = (np.sum(grades) + 120)/(np.size(grades)+2)

print ("mu_1:", mu_1)
print ("mu_2:", mu_2)
print ("mu_3:", mu_3)