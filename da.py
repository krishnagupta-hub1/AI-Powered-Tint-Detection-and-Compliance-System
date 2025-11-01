import cv2  # OpenCV for image processing
import numpy as np
import datetime
import logging
import time

# Set up logging
logging.basicConfig(filename='tint_detection.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class TintDetectionModel:
    def __init__(self):
        # Initialize any parameters or load a pre-trained model here
        pass

    def predict_tint_level(self, image):
        # Convert the image to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define a mask for tinted areas (this is a simplistic approach)
        lower_tint = np.array([0, 0, 0])  # Adjust these values based on the tint you want to detect
        upper_tint = np.array([180, 255, 30])  # Adjust these values based on the tint you want to detect
        mask = cv2.inRange(hsv_image, lower_tint, upper_tint)

        # Calculate the percentage of tinted pixels
        tinted_pixels = cv2.countNonZero(mask)
        total_pixels = image.size / 3  # 3 channels (BGR)

        # Calculate tint level as a percentage
        tint_level = (tinted_pixels / total_pixels) * 100
        return int(tint_level)

def capture_camera_feed(video_path=None):
    # Initialize camera or video capture
    if video_path:
        cap = cv2.VideoCapture(video_path)  # Use the video file
    else:
        cap = cv2.VideoCapture(0)  # Use the first camera device

    if not cap.isOpened():
        print("Error: Could not open camera or video.")
        return None
    return cap

def main(video_path=None):
    legal_limit = 35  # Set the legal limit for tint
    print("System initialized. Legal tint limit: ", legal_limit)

    # Create an instance of the tint detection model
    model = TintDetectionModel()

    # Start capturing video from the camera or video file
    cap = capture_camera_feed(video_path)
    if cap is None:
        return

    start_time = time.time()
    show_tint_level = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Check if 10 seconds have passed
        if time.time() - start_time >= 10:
            show_tint_level = True

        # Simulate tint level detection using the ML model
        tint_level = model.predict_tint_level(frame)

        # Display the tint level on the frame if allowed
        if show_tint_level:
            cv2.putText(frame, f'Tint Level: {tint_level}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Compare detected tint level with the legal limit
            if tint_level > legal_limit:
                alert_message = f"ALERT: Tint level {tint_level}% exceeds legal limit!"
                print(alert_message)
                logging.warning(alert_message)
                cv2.putText(frame, "ALERT: Exceeds Legal Limit!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                normal_message = f"Tint level {tint_level}% is within the legal limit."
                print(normal_message)
                logging.info(normal_message)

        # Show the frame with the tint level
        cv2.imshow('Tint Detection', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting system...")
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()