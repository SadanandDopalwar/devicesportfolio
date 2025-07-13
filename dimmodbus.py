from pymodbus.client.sync import ModbusSerialClient

# Define the USB port where your Modbus device is connected
usb_port = 'COM9'  # Adjust this based on your system

# Create a Modbus RTU client
client = ModbusSerialClient(method='rtu', port=usb_port, baudrate=9600, timeout=1)

# Define the slave ID and address to read from
slave_id = 2
register_address = 1561

# Open the connection
while True:
    if client.connect():
        try:
            # Read holding registers for the specified slave ID and address
            result = client.read_holding_registers(address=register_address, count=10, unit=slave_id)
            
            # Check if the request was successful
            if not result.isError():
                # Print the retrieved data
                print("Data:", result.registers)
                break
            else:
                print("Modbus error:", result)
        except Exception as e:
            print("Exception:", e)
        finally:
            # Close the connection
            client.close()
    else:
        print("Failed to connect to Modbus device at", usb_port)
