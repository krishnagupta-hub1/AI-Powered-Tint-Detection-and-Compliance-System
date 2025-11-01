import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data (make sure the path to your CSV is correct)
data = pd.read_csv('tint_levels_dataset.csv')

# Filter data where tint level exceeds the legal limit (e.g., 35%)
anomalies = data[data['Tint Level (%)'] > 35]

# Print out the anomaly details
print(f"Anomalies Detected (Tint level > 35%):")
print(anomalies)

# Visualize anomalies on the tint level distribution plot
plt.hist(data['Tint Level (%)'], bins=20, color='blue', alpha=0.7)
plt.scatter(anomalies['Frame Number'], anomalies['Tint Level (%)'], color='red', label='Anomalies')
plt.title('Distribution of Tint Levels with Anomalies')
plt.xlabel('Tint Level (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
