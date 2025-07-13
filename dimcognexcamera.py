import socket

def get_dimension_data():
    print("connect_and_get_dimension_data started")
    
    SERVER_IP = '192.168.6.152'  # Change this to the server's IP address
    SERVER_PORT = 23             # Change this to the server's port

    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to server.")

        while True:
            data = 'START'
            client_socket.sendall(data.encode())
            data = client_socket.recv(1024)  # Receive up to 1024 bytes of data
            if not data:
                # If no data is received, the connection is closed by the server
                print("Connection closed by server.")
                break

            # Decode and print the received data
            print("Received:", data.decode())
            break

    except KeyboardInterrupt:
        # Handle Ctrl+C to gracefully close the connection
        print("KeyboardInterrupt: Closing connection.")
        client_socket.close()

    except Exception as e:
        # Handle other exceptions
        print("Error:", e)
        client_socket.close()

# Call the function to connect to the server
get_dimension_data()
