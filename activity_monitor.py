import time
from datetime import datetime
from pynput import mouse, keyboard

from config import Config
from light import Light


class ActivityMonitor:
    def __init__(self):
        self.last_active: datetime = datetime.now()
        self.last_sync: datetime = datetime.now()
        self.light_on: bool = True
        Light.on()
        self.auto_close_inactive: int = Config.instance.auto_close_inactive_seconds

    @property
    def inactivity_threshold(self) -> int:
        return (datetime.now() - self.last_active).seconds

    @property
    def sync_threshold(self) -> int:
        return (datetime.now() - self.last_sync).seconds

    def start_listening(self):
        mouse_listener = mouse.Listener(
            on_move=self._on_active,
            on_click=self._on_active,
            on_scroll=self._on_active
        )
        mouse_listener.daemon = True
        mouse_listener.start()

        keyboard_listener = keyboard.Listener(on_press=self._on_active)
        keyboard_listener.daemon = True
        keyboard_listener.start()

        while True:
            if self.inactivity_threshold > self.auto_close_inactive and self.light_on:
                self.light_on = False
                Light.off()
            if self.sync_threshold > 30:
                self.last_sync = datetime.now()
                self.light_on = Light.get_light_status()
                print("Light sync successful:", self.light_on)

            time.sleep(1)

    def _on_active(self, *args, **kwargs):
        self.last_active = datetime.now()

        if not self.light_on:
            self.light_on = True
            Light.on()
