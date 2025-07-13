import cv2

# Replace 'yourusername' and 'yourpassword' with your camera's username and password
url = "rtsp://admin:Nido@123@192.168.6.153/Streaming/channels/1/"

cap = cv2.VideoCapture()
cap.open(url)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Save the frame as an image
    image_path = r"D:\Images\Images.jpg"  # Specify the path to save the image
  # Specify the path to save the image
    cv2.imwrite(image_path, frame)
    print(f"Image saved to: {image_path}")

    cv2.imshow('frame', frame)
    break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
