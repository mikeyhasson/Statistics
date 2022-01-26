from scipy.stats import norm
from scipy.stats import binom
import math

norm_a=norm(63,math.sqrt(2.5))
print("Q2a: probs =",1-norm_a.cdf(66)+norm_a.cdf(60))

print("Q2b: mu =",60-5*norm.ppf(0.3))

print("Q2c: mu =",60-5*norm.ppf(0.45))

print("Q2f:")
print("probs p_1 =",binom(10,0.55).cdf(5))
print("mu =",(norm.ppf(0.55)+12)/0.2)
print("probs p_2 =",norm(60.6283,math.sqrt(2.5)).cdf(5*(norm.ppf(0.5)+12)))

print("Q2g:")
print("mu =",(norm.ppf(0.5)+12)/0.2)
print("probs p_2 =",norm(60.6283,math.sqrt(2.5)).cdf(5*(norm.ppf(0.5)+12)))


