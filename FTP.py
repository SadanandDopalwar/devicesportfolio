from ftplib import FTP

def connect_to_ftp(ftp_ip, ftp_username, ftp_password, ftp_port=21):
    # Establish FTP connection
    ftp = FTP()
    try:
        ftp.connect(ftp_ip, ftp_port)  # Connect to the FTP server
        ftp.login(ftp_username, ftp_password)  # Log in with username and password
        print(f"Connected to FTP server: {ftp_ip}")
        
        # List directories (optional, just to verify connection)
        ftp.retrlines("LIST")
        
        # Connection is successful
        print("FTP connection successful!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ftp.quit()  # Close the FTP connection
        print("FTP connection closed.")

# Example usage
if __name__ == "__main__":
    ftp_ip = "192.168.5.247"  # Replace with your FTP server IP
    ftp_username = "nidoftp1"  # Replace with your FTP username
    ftp_password = "Nido@123"  # Replace with your FTP password

    connect_to_ftp(ftp_ip, ftp_username, ftp_password)
