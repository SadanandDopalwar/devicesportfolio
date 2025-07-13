import socket
import time

common_delay = 0.1

def get_dimension_data():
    print("connect_and_get_dimension_data started")

    SERVER_IP = '192.168.1.20'
    SERVER_PORT = 3000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to server.")

        while True:
            time.sleep(common_delay)
            client_socket.sendall(bytes("20|01|0001",'utf-8'))
            data = client_socket.recv(1024)
            if not data:
                print("Connection closed by server.")
                break

            print("Received:", data.decode('utf-8'))
            break

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Closing connection.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        print("connect_and_get_dimension_data")

get_dimension_data()


