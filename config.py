import json
from pathlib import Path
from pydantic import BaseModel, Field
import sys

CONFIG_PATH = Path("./config.json")


class Config(BaseModel):
    light_ip: str = Field(default="<light ip>")
    light_token: str = Field(default="<light token>")
    auto_open: bool = Field(default=True)
    auto_close: bool = Field(default=True)
    sync_status_interval: int = Field(default=15)
    auto_close_idle_timeout: int = Field(default=60 * 20)

    instance: "Config" = Field(default=None, exclude=True)

    @classmethod
    def read(cls) -> None:
        if not CONFIG_PATH.exists():
            cls.instance = Config()
            cls.write()
            print("Config not found, generating default config...")
            sys.exit()

        with open(CONFIG_PATH, "rt") as f:
            cls.instance = cls.model_validate(json.loads(f.read()))

    @classmethod
    def write(cls) -> None:
        with open(CONFIG_PATH, "wt") as f:
            f.write(cls.instance.model_dump_json(indent=2))
