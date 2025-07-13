import speech_recognition as sr
import pytesseract
from PIL import ImageGrab
import pyttsx3
import pyautogui
import pyperclip
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("🎤 Voice Assistant is running... (say 'exit' to stop)")

def read_latest_whatsapp_message():
    # Step 1: Open WhatsApp
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("whatsapp")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)  # Wait for WhatsApp to open
    pyautogui.write("Sada")
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("enter")
    engine.say("Opening WhatsApp")
    engine.runAndWait()
    
    time.sleep(3)  # Wait for WhatsApp to open fully

    # Step 2: Optional - click on the first chat
    # pyautogui.click(x=200, y=300)  # Adjust based on your screen/chat list position
    # time.sleep(1)

    # Step 3: Capture screen region where messages appear
    # Adjust the box (left, top, right, bottom) based on WhatsApp window position
    screenshot = ImageGrab.grab(bbox=(80, 100, 730, 620))  # Adjust these

# Optional: save the screenshot for debugging
    screenshot.save("cropped_live_chat.png")

    # Extract text from the screenshot
    text = pytesseract.image_to_string(screenshot, lang='eng')

    # Output the chat text

    # Step 4: Extract text using OCR
    print("📩 WhatsApp Messages:\n", text)

    # Step 5: Speak out
    engine.say("Here are the latest messages.")
    engine.say(text)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data).lower()
            print("🗣️ You said:", text)
            engine.say("You said: " + text)
            engine.runAndWait()
            
            if "Hi Lily" or "Hello Lily" in text:
                engine.say("Hello! How can I assist you today?")
                engine.runAndWait()
            if "read whatsapp" in text:
                read_latest_whatsapp_message()
            if "open chrome" in text:
                engine.say("Opening Chrome")
                engine.runAndWait()

                pyautogui.press("win")
                time.sleep(1)

                pyperclip.copy("chrome")
                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.5)
                pyautogui.press("enter")
            
            if "open whatsapp" in text:
                engine.say("Opening WhatsApp")
                engine.runAndWait()

                pyautogui.press("win")
                time.sleep(1)

                pyperclip.copy("whatsapp")
                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.5)
                pyautogui.press("enter")

            elif "exit" in text:
                engine.say("Goodbye!")
                engine.runAndWait()
                print("👋 Exiting program.")
                break

        except sr.UnknownValueError:
            print("❌ Could not understand.")
            engine.say("Sorry, I did not understand what you said.")
            engine.runAndWait()
        except sr.RequestError:
            print("⚠️ API unavailable.")
            engine.say("There was an issue with the speech recognition service.")
            engine.runAndWait()
