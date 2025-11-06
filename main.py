from activity_monitor import ActivityMonitor
from config import Config

if __name__ == "__main__":
    Config.read()
    monitor = ActivityMonitor()

    try:
        monitor.start_listening()
    except KeyboardInterrupt:
        print("Monitor exit by Ctrl+C")