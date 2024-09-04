import numpy as np

data = [23, 25, 27, 6,22, 30, 31, 29, 24, 28, 26, 8, 99]

mean = np.mean(data)
std_dev = np.std(data)

z_scores = [(x - mean) / std_dev for x in data]

print(f"Z-Scores: {z_scores}")

for i, z in enumerate(z_scores):
    if z > 0:
        direction = "above"
    elif z < 0:
        direction = "below"
    else:
        direction = "at"

    outlier_status = "Outlier" if abs(z) > 3 else "Not an Outlier"
    print(f" {data[i]} is {z:.2f} -{outlier_status}")