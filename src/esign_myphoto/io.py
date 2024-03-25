from pathlib import Path

import tomlkit
import logging as log
from tomlkit.items import Table, String

from esign_myphoto import i18n
from esign_myphoto.config import SigConfig


def load_lang_code(file: Path) -> str:
    try:
        with open(file, mode="rt", encoding="utf-8") as config_file:
            config = tomlkit.load(config_file)

            if "language" in config and isinstance(config["language"], String):
                if str(config["language"]).lower() == "el":
                    return "el"
            return "en"
    except FileNotFoundError:
        return "en"


def load_sig_config(file: Path) -> SigConfig | None:
    try:
        with open(file, mode="rt", encoding="utf-8") as config_file:
            config = tomlkit.load(config_file)

            if "signature" in config and isinstance(config["signature"], Table):
                sig_config = SigConfig(config["signature"])

                if sig_config.license and sig_config.reason:
                    return sig_config
            else:
                log.error(i18n.tr.MSG_SIG_TABLE_MISSING)
    except FileNotFoundError as exc:
        log.error(i18n.tr.MSG_CONFIG_FILE_NOT_FOUND, exc_info=exc)
    return None
