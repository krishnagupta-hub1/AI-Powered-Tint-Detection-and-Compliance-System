import pandas as pd
import re
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

# Plotting the histogram of tint levels
log_data['tint_level'].plot(kind='hist', bins=20, title='Distribution of Tint Levels')
plt.axvline(x=35, color='r', linestyle='--', label='Legal Limit (35%)')  # Line at 35%
plt.xlabel('Tint Level (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
