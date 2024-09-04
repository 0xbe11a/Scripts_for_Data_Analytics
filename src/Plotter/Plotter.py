import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, mean, skewness):

    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, bins=10, color='skyblue')

    plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(mean + skewness * np.std(data), color='green', linestyle='--', label=f'Skew Influence')

    plt.title('Data Distribution with Skewness and Kurtosis')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.legend()

    plt.show()