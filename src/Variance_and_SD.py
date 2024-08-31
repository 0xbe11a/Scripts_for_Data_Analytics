import numpy as np

data = [10, 12, 14, 14, 18, 20, 22, 25, 30, 35, 100, -20]

variance = np.var(data, ddof=0)  # Population variance
# Use ddof=1 for sample variance instead of population variance

std_dev = np.std(data, ddof=0)  # Population standard deviation
# Use ddof=1 for sample standard deviation instead of population standard deviation

# Print the results
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")