from ftplib import FTP

def upload_image_to_ftp(image_path, ftp_ip, ftp_username, ftp_password, ftp_port=21):
    # Establish FTP connection
    ftp = FTP()
    try:
        # Connect to the FTP server
        ftp.connect(ftp_ip, ftp_port)
        ftp.login(ftp_username, ftp_password)
        print(f"Connected to FTP server {ftp_ip}.")
        
        # Open the image file in binary mode
        with open(image_path, 'rb') as file:
            # Upload the image using the STOR command
            ftp.storbinary(f"STOR {image_path.split('/')[-1]}", file)
            print(f"Successfully uploaded {image_path} to the FTP server.")
        
    except Exception as e:
        print(f"Error during FTP upload: {e}")
    finally:
        # Close the FTP connection
        ftp.quit()
        print("FTP connection closed.")

# Main function to call the upload
if __name__ == "__main__":
    image_path = "/home/nido/barcode_image.jpg"  # Replace with the path to your image
    ftp_ip = "192.168.5.247"  # Replace with your FTP server IP
    ftp_username = "nidoftp"  # Replace with your FTP username
    ftp_password = "nido1234"  # Replace with your FTP password

    # Upload the image to the FTP server
    upload_image_to_ftp(image_path, ftp_ip, ftp_username, ftp_password)

