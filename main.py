import win32con
import win32gui
import time

from activity_monitor import ActivityMonitor
from config import Config

if __name__ == "__main__":
    

    Config.read()
    monitor = ActivityMonitor()

    time.sleep(1)
    console_window = win32gui.GetForegroundWindow()
    if console_window:
        win32gui.ShowWindow(console_window, win32con.SW_HIDE)
    
    try:
        monitor.start_listening()
    except KeyboardInterrupt:
        print("Monitor exit by Ctrl+C")
