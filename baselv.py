import pandas as pd
import matplotlib.pyplot as plt

# Read the tint levels CSV file
data = pd.read_csv('tint_levels_dataset.csv')

# Calculate the mean and standard deviation of tint levels
mean_tint = data['Tint Level (%)'].mean()
std_tint = data['Tint Level (%)'].std()

# Plot the histogram to visualize tint levels distribution
plt.hist(data['Tint Level (%)'], bins=20, color='blue', alpha=0.7)
plt.axvline(mean_tint, color='r', linestyle='--', label=f'Mean Tint Level ({mean_tint:.2f}%)')
plt.axvline(mean_tint + std_tint, color='g', linestyle='--', label=f'±1 STD ({mean_tint + std_tint:.2f}%)')
plt.axvline(mean_tint - std_tint, color='g', linestyle='--')
plt.title('Distribution of Tint Levels')
plt.xlabel('Tint Level (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Print baseline statistics
print(f"Mean Tint Level: {mean_tint:.2f}%")
print(f"Standard Deviation: {std_tint:.2f}%")
