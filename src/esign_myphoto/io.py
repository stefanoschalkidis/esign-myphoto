from pathlib import Path

import tomlkit
import logging as log
from tomlkit.items import Table

from esign_myphoto import i18n
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
            else:
                log.error(i18n.tr.MSG_SIG_TABLE_MISSING)
    except FileNotFoundError as exc:
        log.error(i18n.tr.MSG_CONFIG_FILE_NOT_FOUND, exc_info=exc)
    return None
