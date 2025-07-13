from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from fastapi import FastAPI, HTTPException
import uvicorn
import asyncio
from threading import Thread

# Path to the correct version of chromedriver.exe
chrome_driver_path = r"D:\MyFiles\PythonMain\chromedriver-win64\chromedriver.exe"

# URL you want to open
url = 'http://192.168.5.247/maersk'
input_xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
new_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/div/ytd-search-header-renderer/div[1]/yt-chip-cloud-renderer/div/div[2]/iron-selector/yt-chip-cloud-chip-renderer[2]/yt-formatted-string'  # Replace with the actual XPath of the new element

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument('--start-maximized')  # Optional: start browser maximized

# Set up the ChromeDriver service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the URL
    driver.get(url)
    

except webdriver.WebDriverException:
    # Close the browser
    #driver.quit()
    print("Error")


async def read_data(wait):
    try:
            # Wait until the new element is present
            new_element = wait.until(
                EC.presence_of_element_located((By.XPATH, new_xpath))
            )
            
            # Print the text content of the new element
            print("Content of the new element:", new_element.text)
        
    except TimeoutException:
            print("The new element was not found within the timeout period.")


async def click_data(wait):
    try:
            # Specify the XPath of the popup element you want to click
            popup_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/div/ytd-search-header-renderer/div[1]/yt-chip-cloud-renderer/div/div[2]/iron-selector/yt-chip-cloud-chip-renderer[2]/yt-formatted-string"  # Update this to your actual popup XPath
            
            # Wait until the popup element is present
            popup_element = wait.until(
                EC.presence_of_element_located((By.XPATH, popup_xpath))
            )
            
            # Click the popup element
            popup_element.click()
            print("Popup element clicked.")
        
    except TimeoutException:
            print("Popup element was not found within the timeout period.")
async def data_enter(barcode_data):
    try:
        # Use WebDriverWait to wait until the input field is present and visible
        wait = WebDriverWait(driver, 0.1)
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, input_xpath))
        )
        
        # Focus on the input field
        driver.execute_script("arguments[0].focus();", input_field)
        
        # Enter data into the input field
        input_field.send_keys(barcode_data)
        
        # Press Enter to submit the form
        input_field.send_keys(Keys.ENTER)

        
        # Wait for the page to update or navigate
        time.sleep(0.2)
        await read_data(wait)
        time.sleep(0.1)
        await click_data(wait)
                
  
        
        
    
    except TimeoutException:
        print("The input field was not found within the timeout period.")

async def async_process_wrapper1(barcode_data):
    await data_enter(barcode_data)


app = FastAPI()
@app.post('/send-barcode')
async def process_barcode_endpoint(data: dict):
    global barcode_data
    barcode_data = data.get('barcode')
    
    
    if barcode_data:
        # Return success message immediately
        Thread(target=lambda: asyncio.run(async_process_wrapper1(barcode_data))).start()

        return {"Barcode Sent Successfully"}
    else:
        raise HTTPException(status_code=400, detail="Barcode data not provided")


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9021)


