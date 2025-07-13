import serial
import time

z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print(z1serial.is_open)  # True for opened
if z1serial.is_open:
    while True:
        size = z1serial.inWaiting()
        if size:
            data = z1serial.read(size)
            print(data)
            barcode = data.decode('utf-8').strip('b').strip('/r')
            print(barcode)
            
       
        time.sleep(0.1)
else:
    print('z1serial not open')
# z1serial.close()  # close z1serial if z1serial is open.