import numpy as np
import scipy.stats as stats

data = [12, 15, 14, 10, 13, 18, 20, 15, 14, 13]

mean = np.mean(data)

std_dev = np.std(data, ddof=1)  # ddof=1 provides the sample standard deviation

n = len(data)

confidence_level = 0.95

t_critical = stats.t.ppf((1 + confidence_level) / 2, df=n-1)

margin_of_error = t_critical * (std_dev / np.sqrt(n))

confidence_interval = (mean - margin_of_error, mean + margin_of_error)

print(f"Sample Mean: {mean}")
print(f"Sample Standard Deviation: {std_dev}")
print(f"Range which the true population mean is likely to fall, under {confidence_level} confidece level: {confidence_interval}")