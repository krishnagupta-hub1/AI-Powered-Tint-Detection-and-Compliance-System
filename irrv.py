import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset (ensure the path is correct)
data = pd.read_csv('tint_levels_dataset.csv')

# Check the first few rows of the dataset to verify the columns
print(data.head())

# Calculate the z-score to detect outliers
data['z_score'] = zscore(data['Tint Level (%)'])

# Define a threshold for outlier detection (e.g., Z-score > 3 or < -3)
outliers = data[abs(data['z_score']) > 3]

# Display the outliers
print("Detected Outliers:")
print(outliers)

# Visualize outliers on the tint level distribution plot
plt.hist(data['Tint Level (%)'], bins=20, color='blue', alpha=0.7)
plt.scatter(outliers['Frame Number'], outliers['Tint Level (%)'], color='purple', label='Outliers')
plt.title('Distribution of Tint Levels with Outliers')
plt.xlabel('Tint Level (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
