import time
from datetime import datetime
from config import Config
from light import Light
import ctypes
from ctypes import wintypes


class ActivityMonitor:
    def __init__(self):
        self.inactivity_threshold = 0
        self.last_sync: datetime = datetime.now()
        self.light_on: bool = True
        Light.on()
        self.auto_close_inactive: int = Config.instance.auto_close_idle_timeout

    @property
    def sync_threshold(self) -> int:
        return (datetime.now() - self.last_sync).seconds

    def start_listening(self):
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [('cbSize', wintypes.UINT), ('dwTime', wintypes.DWORD)]

        while True:
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            # noinspection PyUnresolvedReferences
            ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo))
            # noinspection PyUnresolvedReferences
            inactive_time = (ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime) // 1000
            if inactive_time < self.inactivity_threshold:
                self._on_active()
            self.inactivity_threshold = inactive_time

            if self.inactivity_threshold > self.auto_close_inactive and self.light_on and Config.instance.auto_close:
                self.light_on = False
                Light.off()

            if self.sync_threshold > Config.instance.sync_status_interval:
                self.last_sync = datetime.now()
                self.light_on = Light.get_light_status()
                print("Light sync successful:", self.light_on)

            time.sleep(1)

    def _on_active(self):
        if not self.light_on and Config.instance.auto_open:
            self.light_on = True
            Light.on()