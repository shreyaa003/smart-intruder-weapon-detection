import cv2
from ultralytics import YOLO
import time
import serial

c1=0
c2=0
c3=0

# Uncomment and configure the serial communication with the device (e.g., Arduino)
ser = serial.Serial("COM5", 9600)  # Replace "COM3" with your serial port and baud rate

# Load the YOLOv8 model
model = YOLO("best.pt")  # Replace "best.pt" with your trained YOLO model

# Open the camera or video file
cap = cv2.VideoCapture(1)  # Use 0 for the default webcam or provide a video file path

# Initialize variables for FPS calculation
prev_time = time.time()

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Create a copy of the frame for annotation
        annotated_frame = frame.copy()

        # Track if any valid detection was found
        valid_detection = False

        # Process detections
        for box in results[0].boxes:
            confidence = float(box.conf)  # Confidence score
            if confidence > 0.8:  # Only process high-confidence detections
                valid_detection = True
                x0, y0, x1, y1 = map(int, box.xyxy[0])  # Bounding box coordinates
                label = int(box.cls)  # Class index
                class_name = model.names[label]  # Class name

                # Draw the bounding box
                cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                cv2.putText(
                    annotated_frame,
                    f"{class_name} {confidence:.2f}",
                    (x0, y0 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    2,
                )

                # Send data based on detected class
                if class_name == 'drinking':
                    ser.write(b'a#')  # Send 'a' to serial port
                    print("Sent 'a#' to serial")
            
                elif class_name in ['softdrink', 'softdrink1']:
                    c2=c2+1
                    if c2== 10:
                        ser.write(b'b#')  # Send 'b' to serial port
                        print("Sent 'b#' to serial")
                        c2=0
                        
                # else:
                #     ser.write(b'c#')  # Send 'c' to serial port
                #     print("Sent 'c#' to serial")

        # If no valid detection was found, send 'c'
        # if not valid_detection:
        #     c3=c3+1
        #     if c3==10:
        #         ser.write(b'c#')  # Send 'c' to serial port
        #         print("Sent 'c#' to serial (no valid detection)")
        #         c3=0

        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        # Add FPS text to the annotated frame
        cv2.putText(
            annotated_frame,
            f"FPS: {fps:.2f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
