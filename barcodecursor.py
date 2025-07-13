import pyautogui
import pyperclip
import time
import socket
import asyncio
import json

file_path = 'settings.json'

# Read the settings from the specified JSON file
with open(file_path, 'r') as f:
    settings = json.load(f)
SERVER_IP = settings.get("cameraip")
SERVER_PORT = settings.get("cameraport")
pastedelay = settings.get("pastedelay")
x = settings.get("xcordinate")
y = settings.get("ycordinate")
coordinatingenabled = settings.get("coordinatingenabled")

async def paste_on_focus(barcode_data):
    if not barcode_data:
        return  # Ignore if barcode_data is None or blank
    await asyncio.sleep(pastedelay)
    
    # Log current position of the cursor
    current_position = pyautogui.position()
    print(f"Current cursor position: {current_position}")
    
    # Move to the specified coordinates
    if coordinatingenabled:
        print(f"Moving cursor to coordinates ({x}, {y})")
        pyautogui.moveTo(x, y, duration=1)  # Adding a duration for smooth movement
        
        # Adding a small delay to ensure cursor has moved
        await asyncio.sleep(0.5)
        
        # Log new position of the cursor
        new_position = pyautogui.position()
        print(f"New cursor position: {new_position}")
        
        # Ensure the cursor is at the new position before clicking
        if new_position == (x, y):
            # Click at the specified coordinates
            pyautogui.click()
            
            # Copy the data to clipboard
            pyperclip.copy(barcode_data)
            print(f"Copied barcode data to clipboard: {barcode_data}")
            
            # Paste data
            pyautogui.hotkey('ctrl', 'v')  # Use 'command' instead of 'ctrl' on macOS
            
            # Press enter
            pyautogui.press('enter')
        else:
            print("Cursor did not move to the correct position.")

    else:
        pyautogui.click()
            
        # Copy the data to clipboard
        pyperclip.copy(barcode_data)
        print(f"Copied barcode data to clipboard: {barcode_data}")
            
        # Paste data
        pyautogui.hotkey('ctrl', 'v')  # Use 'command' instead of 'ctrl' on macOS
            
        # Press enter
        pyautogui.press('enter')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
async def connect_barcode():
    print("Trying to Connect")
    try:      
        # Connect to the barcode camera
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to barcode camera.")

        while True:
            data = client_socket.recv(1024)
            # Decode and print the received data

            print("Received:", data.decode())
            barcode_received = data.decode().strip()
            barcode_array = barcode_received.split(',')
            barcode_data = barcode_array[0]
            #barcode_data = ']d1,5|\MS11198820895|O|FRK/GGN|S|O|03|P|S|F|78,]C0,SF103'
            print("Barcode Printed:", barcode_data)
            await paste_on_focus(barcode_data)
            

    except socket.error as e:
        print(f"Error connecting to PLC: {e}")
        

    finally:
        
        # Close the socket
        client_socket.close()
        print("Closing Socket")


asyncio.run(connect_barcode())
