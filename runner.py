import serial
import time

# Use COM7, and adjust to your desired settings
USB_PORT = 'COM4'
BAUD_RATE = 38400  # Baud rate as specified
DATA_BITS = 8       # Data bits
PARITY = serial.PARITY_NONE  # No parity
STOP_BITS = serial.STOPBITS_ONE  # One stop bit

try:
    # Open serial port with the specified parameters
    with serial.Serial(USB_PORT, BAUD_RATE, timeout=1, bytesize=DATA_BITS, parity=PARITY, stopbits=STOP_BITS) as ser:
        if ser.is_open:
            # Carriage Byte Command
            carriage_byte = bytes([133, 65, 116, 0, 100, 4, 101, 48])
            ser.write(carriage_byte)
            print("Sending command")
            # time.sleep(0.1)  # Sleep for 100ms

            # Carriage Run Command
            # carriage_byte_run = bytes([138, 1, 0, 0, 0, 0, 1, 0])
            # ser.write(carriage_byte_run)
            #b = "84 41 64 00 64 78 30 09"
            # b = "95 01 46 00 4C 02 00 09"
            # carriage_byte = bytes.fromhex(b)
            # ser.write(carriage_byte)
            # print("Sending command")
            time.sleep(0.1)  # 
            s = "8A 01 00 00 00 00 00 01"
            carriage_byte_run = bytes.fromhex(s)
            ser.write(carriage_byte_run)
            print("Commands sent successfully.")
except serial.SerialException as e:
    print(f"Error: {e}")


# Right Slow
# b = "95 01 46 00 4C 02 00 09"
#             carriage_byte = bytes.fromhex(b)
#             ser.write(carriage_byte)
#             print("Sending command")
#             time.sleep(0.1)  # 
#             s = "8A 01 00 00 00 00 00 01"
#             carriage_byte_run = bytes.fromhex(s)
#             ser.write(carriage_byte_run)
#             print("Commands sent successfully.")


#Left Fast
# carriage_byte = bytes([133, 65, 116, 0, 100, 4, 101, 48])
#             ser.write(carriage_byte)
#             print("Sending command")


# time.sleep(0.1)  # 
#             s = "8A 01 00 00 00 00 00 01"
#             carriage_byte_run = bytes.fromhex(s)
#             ser.write(carriage_byte_run)
#             print("Commands sent successfully.")