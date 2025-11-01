import cv2
import numpy as np
import csv
from playsound import playsound

class TintDetectionModel:
    def __init__(self):
        pass

    def predict_tint_level(self, image):
        # Convert the image to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define a mask for tinted areas
        lower_tint = np.array([0, 0, 0])  # Adjust based on tint detection criteria
        upper_tint = np.array([180, 255, 30])  # Adjust based on tint detection criteria
        mask = cv2.inRange(hsv_image, lower_tint, upper_tint)

        # Calculate the percentage of tinted pixels
        tinted_pixels = cv2.countNonZero(mask)
        total_pixels = image.shape[0] * image.shape[1]  # Total number of pixels (rows * cols)

        # Calculate tint level as a percentage
        tint_level = (tinted_pixels / total_pixels) * 100
        return int(tint_level)

def check_tint_level_from_video(video_path, output_csv):
    if video_path is None:
        print("Error: No video file path provided.")
        return

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Video properties
    frame_width = 1500
    frame_height = 850
    fps = 25
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = total_frames / fps

    # Create an instance of the tint detection model
    model = TintDetectionModel()

    # Prepare CSV file for saving results
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Frame Number', 'Tint Level (%)'])

        # Frame processing
        legal_limit = 35
        frame_count = 0
        fine_printed = False  # Flag to ensure fine message is printed only once

        while frame_count < total_frames:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Resize the frame to the target resolution
            frame = cv2.resize(frame, (frame_width, frame_height))

            # Analyze tint level
            tint_level = model.predict_tint_level(frame)

            # Save the tint level for the frame to the CSV file
            writer.writerow([frame_count, tint_level])

            # Display the frame with annotations
            cv2.putText(frame, f'Tint Level: {tint_level}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if tint_level > legal_limit:
                cv2.putText(frame, "ALERT: Exceeds Legal Limit!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # Play buzzer sound
                playsound('buzzer-227217.mp3')  # Replace 'buzzer.mp3' with the path to your sound file

                # Print fine message only once
                if not fine_printed:
                    print("ALERT: Tint level exceeds legal limit. Fine imposed: ₹5000.")
                    fine_printed = True  # Prevent further printing of the fine message

            # Show the frame
            cv2.imshow('Tint Detection', frame)
            # Exit on 'q' key press
            if cv2.waitKey(1000 // fps) & 0xFF == ord('q'):
                print("Exiting system...")
                break

            frame_count += 1

    # Release the video and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print(f"Tint levels saved to {output_csv}")

if __name__ == "__main__":
    # Specify the video file path and output CSV file path
    video_file_path = '12687614_1080_1920_60fps.mp4'
    output_csv_path = 'tint_levels_dataset.csv'
    check_tint_level_from_video(video_file_path, output_csv_path)
