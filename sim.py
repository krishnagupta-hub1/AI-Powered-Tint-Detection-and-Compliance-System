import random
import time

# Simulated functions for the system components
def capture_vehicle_image():
    print("Capturing vehicle image...")
    # Mock image data
    return {"vehicle_id": random.randint(1000, 9999), "image_data": "mock_image_data"}

def analyze_tint(image_data):
    print("Analyzing tint level from image data...")
    # Simulating visible light transmission (VLT) detection
    tint_level = random.uniform(30, 100)  # Mock VLT percentage
    return tint_level

def check_compliance(tint_level):
    legal_vlt = 70  # Legal VLT threshold for demonstration
    if tint_level < legal_vlt:
        return False, legal_vlt - tint_level
    return True, 0

def transmit_data(vehicle_id, tint_level, compliance_status, server="central_dashboard"):
    print(f"Transmitting data to {server}...")
    # Mock transmission to server
    return {
        "vehicle_id": vehicle_id,
        "tint_level": tint_level,
        "compliance": compliance_status,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

def display_on_dashboard(data):
    print("\n--- Real-Time Dashboard ---")
    print(f"Vehicle ID: {data['vehicle_id']}")
    print(f"Tint Level Detected: {data['tint_level']}%")
    print("Compliance Status:", "Compliant" if data['compliance'] else "Violation")
    print(f"Timestamp: {data['timestamp']}")
    print("--------------------------\n")

# Main demonstration loop
def main_demo():
    print("Starting IoT-Enabled Tint Detection System...\n")
    for _ in range(5):  # Simulate for 5 vehicles
        image_data = capture_vehicle_image()
        vehicle_id = image_data["vehicle_id"]
        tint_level = analyze_tint(image_data["image_data"])
        compliance, violation_margin = check_compliance(tint_level)
        
        if not compliance:
            print(f"Alert: Vehicle {vehicle_id} violates tint regulations by {violation_margin:.2f}%.")
        
        transmitted_data = transmit_data(vehicle_id, tint_level, compliance)
        display_on_dashboard(transmitted_data)
        time.sleep(2)  # Simulate delay between vehicle checks

# Run the demo
if __name__ == "__main__":
    main_demo()
