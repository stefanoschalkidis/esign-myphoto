import sys
from pathlib import Path

import tomlkit
from tomlkit.items import Table

from esign_myphoto.config import SigConfig

root_path = Path(__file__).parent.parent

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    root_path = Path(sys.executable).parent

if __name__ == "__main__":
    with open(
        root_path / "config/config.toml", mode="rt", encoding="utf-8"
    ) as config_file:
        toml_config = tomlkit.load(config_file)

        if "signature" in toml_config and isinstance(toml_config["signature"], Table):
            sig_config = SigConfig(toml_config["signature"])

            if sig_config.license and sig_config.reason:
                print("Hello")
