import cv2

def stream_dual_video(camera_index1, camera_index2):
    # Initialize both cameras
    cap1 = cv2.VideoCapture(camera_index1)
    cap2 = cv2.VideoCapture(camera_index2)

    # Check if cameras were successfully opened
    if not cap1.isOpened() or not cap2.isOpened():
        print("Error: Could not open one or both cameras.")
        # Release any opened cameras and exit
        cap1.release()
        cap2.release()
        return

    print("Streaming video. Press 'q' to quit.")

    while True:
        # Capture frame-by-frame from both cameras
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("Failed to grab frame from one or both cameras")
            break

        # Display the resulting frames
        cv2.imshow('Camera 1 Stream', frame1)
        cv2.imshow('Camera 2 Stream', frame2)

        # Break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the captures and close all windows
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

# Start streaming from cameras 0 and 1
stream_dual_video(0, 1)
