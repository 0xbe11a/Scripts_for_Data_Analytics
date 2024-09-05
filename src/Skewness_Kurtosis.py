import numpy as np
from scipy.stats import skew, kurtosis
import seaborn as sns
from Plotter.Plotter import plot_distribution

# Dataset
data = [10, 12, 14, 14, 18, 20, 22, 25, 30, 35, 100, -20]

mean = np.mean(data)
skewness = skew(data)
kurt = kurtosis(data)

if skewness > 0:
    skew_direction = "positive"
elif skewness < 0:
    skew_direction = "negative"
else:
    skew_direction = "zero (symmetric)"

# Determine kurtosis type
if kurt > 0:
    kurt_type = "Leptokurtic (L)"  # Higher peak, fatter tails
elif kurt < 0:
    kurt_type = "Platykurtic (P)"  # Flatter peak, thinner tails
else:
    kurt_type = "Mesokurtic (M)"   # Normal distribution

print(f"Skewness: {skewness} (Skew is {skew_direction})")
print(f"Kurtosis: {kurt} (Kurtosis is {kurt_type})")

plot_distribution(data, mean, skewness)