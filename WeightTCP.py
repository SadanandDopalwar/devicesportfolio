import socket
import traceback

def get_weight_from_tcp(ip, port):
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_client:
            tcp_client.connect((ip, port))

            # Command to request data (equivalent to {0x02, 0x4D, 0x03, 0x0D, 0x0A})
            request_command = bytes([0x02, 0x4D, 0x03, 0x0D, 0x0A])
            tcp_client.sendall(request_command)

            # Receive data
            buffer = tcp_client.recv(1024)
            tcp_data = buffer.decode("ascii").strip()

            print(f"TCP Data Received: {tcp_data}")

            # Extract valid weight data (lines starting with  and containing a numeric value)
            parsed_data = None
            for line in tcp_data.split("\n"):
                line = line.strip()
                if line.startswith("\x02") and "." in line:
                    parsed_data = line.strip("\x02\x03\r")
                    break

            if parsed_data and parsed_data.replace(".", "", 1).isdigit():
                weight_value = float(parsed_data)
                print(f"Parsed Weight: {weight_value} kg")
                return weight_value
            else:
                print("Failed to parse valid weight data.")
                return None
    except Exception as e:
        print("Error:", str(e))
        traceback.print_exc()
        return None

# Example usage
if __name__ == "__main__":
    TCP_IP = "192.168.1.100"  # Change this to your device's IP
    TCP_PORT = 12345  # Change this to your device's port

    weight = get_weight_from_tcp(TCP_IP, TCP_PORT)
    if weight is not None:
        print(f"Weight received: {weight:.2f} kg")
    else:
        print("No valid weight received.")
