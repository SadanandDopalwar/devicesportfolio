import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image):
    img = cv2.imread(image)

    # Decode the barcode image
    detectedBarcodes = decode(img)
    

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        # Traverse through all the detected barcodes in the image
        for barcode in detectedBarcodes:
            # Locate the barcode position in the image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in the image using cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data and type
                print(barcode.data)
                print(barcode.type)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Take the image from user
    image = r"D:\MyFiles\new.jpg"
    BarcodeReader(image)
