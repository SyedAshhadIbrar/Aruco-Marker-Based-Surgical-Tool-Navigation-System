import cv2

# Load the Aruco dictionary and detector parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Open the webcam
cap = cv2.VideoCapture(0) #1 foe Droid Cam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect markers
    corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        if len(ids) == 2:  # If both markers are detected
            # Calculate the center of the two markers
            tool_center = corners[0][0].mean(axis=0)
            target_center = corners[1][0].mean(axis=0)

            # Calculate the distance
            distance = ((tool_center - target_center) ** 2).sum() ** 0.5
            cv2.putText(frame, f'Distance: {int(distance)}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw an arrow from the tool to the target
            cv2.arrowedLine(frame, tuple(tool_center.astype(int)), tuple(target_center.astype(int)), (255, 0, 0), 5)

    # Display the frame
    cv2.imshow('Aruco Marker Detection', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
