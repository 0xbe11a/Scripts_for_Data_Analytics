import numpy as np
from scipy import stats

group1 = [23, 25, 27, 22, 30, 31, 29, 24, 28, 26]
group2 = [35, 32, 37, 34, 36, 33, 38, 35, 39, 31]

var1 = np.var(group1, ddof=1)  # Sample variance for group1
var2 = np.var(group2, ddof=1)  # Sample variance for group2

n1 = len(group1)
n2 = len(group2)

numerator = (var1/n1 + var2/n2)**2
denominator = ( (var1/n1)**2 / (n1 - 1) ) + ( (var2/n2)**2 / (n2 - 1) )
df_unequal_var = numerator / denominator

df_equal_var = n1 + n2 - 2

t_statistic, p_value = stats.ttest_ind(group1, group2)

print(f"Variance of Group 1: {var1}")
print(f"Variance of Group 2: {var2}")
print(f"Degrees of Freedom (Unequal Variances): {df_unequal_var}")
print(f"Degrees of Freedom (Equal Variances): {df_equal_var}")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

# Interpretation
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the group means.")