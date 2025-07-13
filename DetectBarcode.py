import cv2
from pyzbar.pyzbar import decode

def BarcodeReaderFromCamera():
    # Open a connection to the laptop's camera (usually index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'q' to quit.")
    
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Decode barcodes in the frame
        detectedBarcodes = decode(frame)

        for barcode in detectedBarcodes:
            # Extract barcode bounding box coordinates
            (x, y, w, h) = barcode.rect
            # Draw a rectangle around the detected barcode
            cv2.rectangle(frame, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)

            # Print the decoded barcode data and type
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            print(f"Detected Barcode: {barcodeData} | Type: {barcodeType}")

            # Put the barcode data as text on the frame
            cv2.putText(frame, f"{barcodeData} ({barcodeType})", 
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the frame with the barcode rectangle
        cv2.imshow("Barcode Scanner", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    BarcodeReaderFromCamera()
