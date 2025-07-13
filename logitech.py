import cv2
import time

def capture_image(camera_index, width=2448, height=2048):
    """Captures an image from the specified camera index at the given resolution."""
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print(f"Failed to access the camera at index {camera_index}")
        return

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    time.sleep(2)  # Allow camera to adjust
    ret, frame = cap.read()

    if ret:
        filename = f"camera_{camera_index}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename} with resolution {frame.shape[1]}x{frame.shape[0]}")
    else:
        print("Failed to capture image")

    cap.release()
    cv2.destroyAllWindows()

# Change camera_index if needed
camera_index = 1  # Adjust based on your detected camera
capture_image(camera_index)



#For Ubuntu
#sudo apt install v4l-utils

# import cv2
# import time

# cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Force V4L2

# if not cap.isOpened():
#     print("Failed to access the camera at index 0")
# else:
#     time.sleep(2)  # Allow the camera to adjust
#     ret, frame = cap.read()
#     if ret:
#         cv2.imwrite("test.jpg", frame)
#         print("Image saved as test.jpg")
#     else:
#         print("Failed to capture image")
#     cap.release()
#     cv2.destroyAllWindows()

