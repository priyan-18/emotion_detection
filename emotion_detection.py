import cv2
from fer import FER

# Initialize FER emotion detector
emotion_detector = FER() 


# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 is the default camera


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the frame
    result = emotion_detector.detect_emotions(frame)

    for face in result:
        # Get bounding box for the detected face
        (x, y, w, h) = face["box"]
        # Get the emotion with the highest confidence
        emotion, score = max(face["emotions"].items(), key=lambda item: item[1])

        # Draw rectangle around face and display the highest confidence emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"{emotion} ({score:.2f})", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the video frame with detected emotions
    cv2.imshow("Emotion Detection", frame)

    # Press 'q' to exit the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()


