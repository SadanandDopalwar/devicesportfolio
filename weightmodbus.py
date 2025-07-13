from pymodbus.client.sync import ModbusSerialClient

# Define the USB port where your Modbus device is connected
usb_port = 'COM5'  # Adjust this based on your system

client = ModbusSerialClient(method='rtu', port=usb_port, baudrate=9600, timeout=1)
# Create a Modbus RTU client
# client = ModbusSerialClient(
#     method='rtu', 
#     port=usb_port, 
#     baudrate=9600, 
#     timeout=1, 
#     parity='N'  # Set parity to None ('N'), even ('E'), or odd ('O')
# )

# Open the connection
while True:
    if client.connect():
        try:
            # Read holding registers starting from address 0, read 2 registers
            result = client.read_holding_registers(address=0, count=2, unit=1)
            
            # Check if the request was successful
            if not result.isError():
                # Print the retrieved data
                print("Data:", result.registers)
            else:
                print("Modbus error:", result)
        except Exception as e:
            print("Exception:", e)
        finally:
            # Close the connection
            client.close()
    else:
        print("Failed to connect to Modbus device at", usb_port)
