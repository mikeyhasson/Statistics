from scipy.stats import norm
import math

expected_weight =81.5
deviation_weight = 13.0
probs = 1 - norm.cdf ([82.0],loc=expected_weight,scale=deviation_weight)
print("Question 3a:", probs)

n=50
probs_all_n = pow(probs,n)
print("Question 3b:", probs_all_n)

#By the Central Limit Theorem
probs_mean_smaller = norm.cdf([82.0],loc=expected_weight,scale=deviation_weight/math.sqrt(n))
probs_mean_bigger = 1-probs_mean_smaller

print("Question 3c:", probs_mean_bigger)

n=25
probs_mean_smaller_82 = norm.cdf([82.0],loc=expected_weight,scale=deviation_weight/math.sqrt(n))
probs_mean_smaller_80 = norm.cdf([80.0],loc=expected_weight,scale=deviation_weight/math.sqrt(n))
probs_mean_between_80_82 = probs_mean_smaller_82 - probs_mean_smaller_80
print("Question 3d:", probs_mean_between_80_82)


print("Question 3e:", norm.ppf([0.9],loc=expected_weight,scale=deviation_weight))

#We know the weight distribution is normal
seventy_percentile = 90
twenty_percentile = 70

print("Question 3f: phi^-1 of [0.2,0.7] is", norm.ppf([0.2,0.7]))