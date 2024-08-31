import numpy as np
from scipy.stats import f_oneway

group1 = [23, 25, 27, 22, 30, 31, 29, 24, 28, 26]
group2 = [35, 32, 37, 34, 36, 33, 38, 35, 39, 31]
group3 = [48, 45, 47, 44, 46, 49, 48, 47, 43, 45]
group4 = [56, 52, 54, 55, 58, 59, 60, 57, 53, 51]
group5 = [63, 65, 67, 66, 68, 62, 64, 69, 61, 66]

f_statistic, p_value = f_oneway(group1, group2, group3, group4, group5)

print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: At least one group mean is significantly different.")
else:
    print("Fail to reject the null hypothesis: No significant difference between group means.")