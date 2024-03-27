import base64
import re
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path

import tomlkit
import logging as log

from PIL import Image
from tomlkit.items import Table, String

from esign_myphoto import i18n
from esign_myphoto.config import SigConfig

INVALID_CHARACTERS = '[\\\\/:*?"<>|]'


@dataclass
class Person:
    last_name: str
    first_name: str


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


def prompt_for_signer() -> Person:
    last_name = input(i18n.tr.QUESTION_ENTER_LAST_NAME).strip()

    while re.search(INVALID_CHARACTERS, last_name) or not last_name:
        if re.search(INVALID_CHARACTERS, last_name):
            log.warning(i18n.tr.MSG_INVALID_CHARACTER_ENTERED)
        last_name = input(i18n.tr.QUESTION_ENTER_LAST_NAME).strip()

    first_name = input(i18n.tr.QUESTION_ENTER_FIRST_NAME).strip()

    while re.search(INVALID_CHARACTERS, first_name) or not first_name:
        if re.search(INVALID_CHARACTERS, first_name):
            log.warning(i18n.tr.MSG_INVALID_CHARACTER_ENTERED)
        first_name = input(i18n.tr.QUESTION_ENTER_FIRST_NAME).strip()

    return Person(last_name, first_name)


def save_signature(sig_data: str, signer: Person, root_path: Path) -> bool:
    try:
        save_path = root_path / "output"
        save_path.mkdir(parents=True, exist_ok=True)
        date = datetime.today().strftime("%Y%m%d")
        file_path = save_path / f"{date}_{signer.last_name}_{signer.first_name}.jpg"
        image = Image.open(BytesIO(base64.b64decode(sig_data)))
        image.save(file_path)
        log.info(i18n.tr.MSG_SIGNATURE_SAVED)
        return True
    except Exception:
        log.error(i18n.tr.ERR_DURING_SIG_SAVING)
        return False
