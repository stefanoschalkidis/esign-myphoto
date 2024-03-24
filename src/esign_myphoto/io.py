from pathlib import Path

import tomlkit
import logging as log
from tomlkit.items import Table

from esign_myphoto.config import SigConfig


def load_sig_config(file_path: Path) -> SigConfig | None:
    try:
        with open(file_path, mode="rt", encoding="utf-8") as config_file:
            toml_config = tomlkit.load(config_file)

            if "signature" in toml_config and isinstance(
                toml_config["signature"], Table
            ):
                sig_config = SigConfig(toml_config["signature"])

                if sig_config.license and sig_config.reason:
                    return sig_config
    except FileNotFoundError:
        log.error("Configuration file does not exist.")
    return None
