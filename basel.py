import pandas as pd
import re

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

# Analytics
if not log_data.empty:
    avg_tint_level = log_data['tint_level'].mean()
    max_tint_level = log_data['tint_level'].max()
    min_tint_level = log_data['tint_level'].min()
    non_compliant_count = log_data[log_data['status'] == "Non-Compliant"].shape[0]

    print(f"Average Tint Level: {avg_tint_level:.2f}%")
    print(f"Maximum Tint Level: {max_tint_level}%")
    print(f"Minimum Tint Level: {min_tint_level}%")
    print(f"Number of Non-Compliant Entries: {non_compliant_count}")
else:
    print("No valid data found in the log file.")
