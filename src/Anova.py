import numpy as np
from scipy.stats import f_oneway
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

group1 = [23, 25, 27, 22, 30, 31, 29, 24, 28, 26]
group2 = [35, 32, 37, 34, 36, 33, 38, 35, 39, 31]
group3 = [48, 47, 46, 45, 47, 48, 47, 46, 45, 47]  
group4 = [56, 52, 54, 55, 58, 59, 60, 57, 53, 51]
group5 = [49, 50, 48, 47, 49, 50, 49, 48, 50, 49] 


f_statistic, p_value = f_oneway(group1, group2, group3, group4, group5)

print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: At least one group mean is significantly different.")
else:
    print("Fail to reject the null hypothesis: No significant difference between group means.")


data = np.concatenate([group1, group2, group3, group4, group5])

groups = ['Group 1'] * len(group1) + ['Group 2'] * len(group2) + ['Group 3'] * len(group3) + ['Group 4'] * len(group4) + ['Group 5'] * len(group5)

tukey_result = pairwise_tukeyhsd(data, groups, alpha=0.05)

print(tukey_result) 