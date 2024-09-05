import numpy as np
import scipy.stats as stats

data = [12, 15, 14, 10, 13, 18, 20, 15, 14, 13]

mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # ddof=1 provides the sample standard deviation
n = len(data)
confidence_level = 0.90

t_critical = stats.t.ppf((1 + confidence_level) / 2, df=n-1)
margin_of_error = t_critical * (std_dev / np.sqrt(n))
confidence_interval = (float(mean - margin_of_error), float(mean + margin_of_error))

print(f"From Sampling - Under {100*confidence_level:.2f}% confidence level: Range to fall in Population: {confidence_interval}")