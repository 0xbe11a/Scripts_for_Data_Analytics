import numpy as np

#data = [10, 12, 14, 14, 18, 20, 22, 25, 30, 35, 100, -20]
#data = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
data = [11, 12, 13, 9, 8, 10, 14, 20, 10, 17]

mean = np.mean(data)
variance = np.var(data, ddof=0)  
std_dev = np.std(data, ddof=0)  

print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

if std_dev < 10: #important condition
    interpretation = "Close around the mean."
elif std_dev < 20:
    interpretation = "Moderate Spread around the mean."
else:
    interpretation = "Significant Spread around the mean."

print(f"Interpretation: {interpretation}")