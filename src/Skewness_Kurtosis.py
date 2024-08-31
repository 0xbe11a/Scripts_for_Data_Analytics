import numpy as np
from scipy.stats import skew, kurtosis

data = [10, 12, 14, 14, 18, 20, 22, 25, 30, 35, 100, -20]

skewness = skew(data)

if skewness > 0:
    skew_direction = "positive"
elif skewness < 0:
    skew_direction = "negative"
else:
    skew_direction = "zero (symmetric)"

kurt = kurtosis(data)

if kurt > 0:
    kurt_type = "Leptokurtic (L)"  # Higher peak, fatter tails
elif kurt < 0:
    kurt_type = "Platykurtic (P)"  # Flatter peak, thinner tails
else:
    kurt_type = "Mesokurtic (M)"   # Normal distribution

# Print the results
print(f"Skewness: {skewness} (Skew is {skew_direction})")
print(f"Kurtosis: {kurt} (Kurtosis is {kurt_type})")