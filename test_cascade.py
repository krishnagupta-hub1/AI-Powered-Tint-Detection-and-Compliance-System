import cv2

# Load the cascade
vehicle_cascade = cv2.CascadeClassifier(r'C:\Users\parth\tint\haarcascade_car.xml')

# Check if it loaded successfully
if vehicle_cascade.empty():
    raise FileNotFoundError("Haar cascade file could not be loaded.")

print("Haar cascade loaded successfully!")
