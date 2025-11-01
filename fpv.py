import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data (ensure the file path is correct)
data = pd.read_csv('tint_levels_dataset.csv')

# Check the first few rows to verify the data
print(data.head())

# Prepare the data for prediction (use frame number as the feature and tint level as the target)
X = data['Frame Number'].values.reshape(-1, 1)  # Independent variable: frame number
y = data['Tint Level (%)'].values  # Dependent variable: tint level

# Train a linear regression model to predict future tint levels
model = LinearRegression()
model.fit(X, y)

# Predict future tint levels (for example, next 10 frames)
future_frames = np.array([data['Frame Number'].max() + i for i in range(1, 11)]).reshape(-1, 1)
future_tints = model.predict(future_frames)

# Plot the predictions
plt.plot(data['Frame Number'], data['Tint Level (%)'], label='Historical Tint Levels')
plt.plot(future_frames, future_tints, label='Predicted Tint Levels', linestyle='--', color='orange')
plt.title('Tint Level Prediction')
plt.xlabel('Frame Number')
plt.ylabel('Tint Level (%)')
plt.legend()
plt.show()

# Print future predictions
print("Predicted Future Tint Levels:")
for frame, tint in zip(future_frames.flatten(), future_tints):
    print(f"Frame {frame}: {tint:.2f}%")
