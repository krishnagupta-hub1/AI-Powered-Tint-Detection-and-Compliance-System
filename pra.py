import pandas as pd
import re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Function to extract tint levels from log lines
def extract_tint_level(line):
    match = re.search(r'Tint level (\d+)%', line)
    if match:
        return int(match.group(1))
    return None

# Read the log file
log_file = 'tint_detection.log'
with open(log_file, 'r') as f:
    log_lines = f.readlines()

# Extract timestamp, tint level, and status
data = []
for line in log_lines:
    try:
        timestamp = line.split(':INFO:')[0]  # Extract the timestamp
        tint_level = extract_tint_level(line)  # Extract the tint level
        status = "Compliant" if "within the legal limit" in line else "Non-Compliant"
        if tint_level is not None:  # Only include lines with valid tint levels
            data.append([timestamp, tint_level, status])
    except Exception as e:
        print(f"Error parsing line: {line}. Error: {e}")

# Create a DataFrame
log_data = pd.DataFrame(data, columns=['timestamp', 'tint_level', 'status'])

# Convert timestamp to datetime for proper plotting and processing
log_data['timestamp'] = pd.to_datetime(log_data['timestamp'], errors='coerce')

# Ensure there is data
if not log_data.empty:
    # Convert timestamp to numerical values (e.g., Unix timestamp)
    log_data['timestamp'] = log_data['timestamp'].apply(lambda x: x.timestamp() if pd.notnull(x) else 0)

    # Prepare data for training
    X = log_data[['timestamp']].values.reshape(-1, 1)  # Convert timestamp to numerical values
    y = log_data['tint_level'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict future tint levels on the test set
    future_tint = model.predict(X_test)
    print(f"Predicted Future Tint Levels: {future_tint}")
    
    # Optionally plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(log_data['timestamp'], log_data['tint_level'], label='Tint Level')
    plt.axhline(y=35, color='r', linestyle='--', label='Legal Limit')
    plt.xlabel('Time')
    plt.ylabel('Tint Level (%)')
    plt.title('Tint Level Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("No valid data found in the log file.")
