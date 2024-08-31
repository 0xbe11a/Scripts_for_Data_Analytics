import numpy as np

data = [23, 25, 27, 22, 30, 31, 29, 24, 28, 26]

mean = np.mean(data)
std_dev = np.std(data)

z_scores = [(x - mean) / std_dev for x in data]

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(f"Z-Scores: {z_scores}")

for i, z in enumerate(z_scores):
    if z > 0:
        direction = "above"
    elif z < 0:
        direction = "below"
    else:
        direction = "at"
    print(f"Data point {data[i]} is {z:.2f} standard deviations {direction} the mean.")