# import socket

# # Printer's IP address and port
# printer_ip = '192.168.1.102'  # Replace with your printer's IP address
# printer_port = 9100  # Replace with the appropriate port number



# # Commands to print
# commands = """
# SIZE 4,2
# DIRECTION 0,0
# REFERENCE 0,0
# OFFSET 0 mm
# SET PEEL OFF
# SET CUTTER OFF
# SET PARTIAL_CUTTER OFF
# SET TEAR ON
# CLS
# CODEPAGE 1252
# BARCODE 550,360,"128M",120,2,180,2.5,4,"X000296011B1"

# PRINT 1,1
# """

# # Create a socket connection to the printer
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as printer_socket:
#     socket.setdefaulttimeout(10)
#     printer_socket.connect((printer_ip, printer_port))
#     print("HII")
#     # Send the commands to the printer
#     printer_socket.sendall(commands.encode('utf-8'))


# # TEXT 750,350,"ROMAN.TTF",180,1,15,"HYDERABAD MIYAPUR -HUB"
# # TEXT 120,350,"ROMAN.TTF",180,1,12,"Surface"
# # TEXT 740,280,"ROMAN.TTF",180,1,15,"22"
# # TEXT 650,280,"ROMAN.TTF",180,1,12,"27.7 kg"
# # TEXT 500,280,"ROMAN.TTF",180,1,10,"1029"
# # TEXT 350,280,"ROMAN.TTF",180,1,10,"05-Sep-2023T18:15:29.105"
# #BARCODE 600,200,"128M",120,2,180,3,5,"DELINK,1012"

# # CODEPAGE 1252
# # TEXT 700,340,"ROMAN.TTF",180,1,20,"LBH(in mm) -{length}x{breadth}x{height} "
# # TEXT 700,260,"ROMAN.TTF",180,1,20,"Volume(in M3) - "
# # TEXT 700,180,"ROMAN.TTF",180,1,20,"{volume}  M3"
# # QRCODE 100,100,H,4.8,A,0, "印表機<Enter>
# # ABC<Enter>
# # abc<Enter>
# # 123"

import socket
import csv

# # Printer's IP address and port
printer_ip = '192.168.1.102'  # Replace with your printer's IP address
printer_port = 9100  # Replace with the appropriate port number

# Path to the CSV file
csv_file_path = 'data.csv'

# Open the CSV file and read the data
with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        barcodes = row[:4]  # Assuming the first 4 columns contain the barcodes
        barcode_commands = "\n".join([f"BARCODE 700,{350+i},\"128M\",120,2,180,3,5,\"{barcode}\"" for i, barcode in enumerate(barcodes)])
        
        # Commands to print
        commands = f"""
        SIZE 4,2
        DIRECTION 0,0
        REFERENCE 0,0
        OFFSET 0 mm
        SET PEEL OFF
        SET CUTTER OFF
        SET PARTIAL_CUTTER OFF
        SET TEAR ON
        CLS
        CODEPAGE 1252
        {barcode_commands}
        PRINT 1,1
        """

        # Create a socket connection to the printer
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as printer_socket:
            socket.setdefaulttimeout(1)
            print(commands)
            printer_socket.connect((printer_ip, printer_port))

            # # Send the commands to the printer
            printer_socket.sendall(commands.encode('utf-8'))