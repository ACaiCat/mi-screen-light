from typing import Optional
from miio import Yeelight
from config import Config


class Light:
    @classmethod
    def get_light(cls) -> Optional[Yeelight]:
        try:
            dev = Yeelight(Config.instance.light_ip, Config.instance.light_token)
        except Exception as ex:
            print("Failed to connect device:", ex)
            return None

        print("Connected.Device info:", dev.info())
        return dev

    @classmethod
    def get_light_status(cls) -> bool:
        dev: Optional[Yeelight] = cls.get_light()
        if dev is None:
            return True

        return dev.status().is_on

    @classmethod
    def on(cls) -> None:
        dev: Optional[Yeelight] = cls.get_light()
        if dev is None:
            return

        dev.on()
        print("Success open the light:", dev.status().is_on)

    @classmethod
    def off(cls) -> None:
        dev: Optional[Yeelight] = cls.get_light()
        if dev is None:
            return

        dev.off()
        print("Success close the light:", dev.status().is_on)
