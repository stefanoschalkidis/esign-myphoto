import base64
import re
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path

import i18n as load_i18n
import tomlkit
import tkinter.messagebox as mb
import logging as log

from PIL import Image
from tomlkit.items import Table, String

from esign_myphoto import i18n
from esign_myphoto.config import SigConfig

INVALID_CHARACTERS = '[\\\\/:*?"<>|]'


def load_lang_code(file: Path) -> str:
    try:
        with open(file, mode="rt", encoding="utf-8") as config_file:
            config = tomlkit.load(config_file)

            if "language" in config and isinstance(config["language"], String):
                if str(config["language"]).lower() == "el":
                    return "el"
            return "en"
    except FileNotFoundError as exc:
        lang_key = "str.msg_config_file_not_found"
        log.error(load_i18n.t(lang_key, locale="en"), exc_info=exc)
        return "en"


@dataclass
class LoadSigConfigResult:
    sig_config: SigConfig
    msg: str | None


def load_sig_config(file: Path) -> LoadSigConfigResult:
    sig_config = SigConfig(tomlkit.table())
    msg = None

    try:
        with open(file, mode="rt", encoding="utf-8") as config_file:
            config = tomlkit.load(config_file)

            if "signature" in config and isinstance(config["signature"], Table):
                sig_config = SigConfig(config["signature"])

                if not sig_config.license or not sig_config.reason:
                    lang_key = "str.err_license_or_reason_not_defined"
                    log.error(load_i18n.t(lang_key, locale="en"))
                    msg = i18n.tr.ERR_LICENSE_OR_REASON_NOT_DEFINED
            else:
                lang_key = "str.msg_sig_table_missing"
                log.error(load_i18n.t(lang_key, locale="en"))
                msg = i18n.tr.MSG_SIG_TABLE_MISSING
    except FileNotFoundError as exc:
        lang_key = "str.msg_config_file_not_found"
        log.error(load_i18n.t(lang_key, locale="en"), exc_info=exc)
        msg = i18n.tr.MSG_CONFIG_FILE_NOT_FOUND

    return LoadSigConfigResult(sig_config, msg)


def are_input_names_valid(last_name: str, first_name: str) -> bool:
    if not last_name or not first_name:
        mb.showinfo(i18n.tr.TITLE_INFORMATION, i18n.tr.MSG_PLEASE_COMPLETE_ALL_FIELDS)
        return False

    if re.search(INVALID_CHARACTERS, last_name) or re.search(
        INVALID_CHARACTERS, first_name
    ):
        mb.showinfo(i18n.tr.TITLE_INFORMATION, i18n.tr.MSG_INVALID_CHARACTER_ENTERED)
        return False
    return True


@dataclass
class SaveResult:
    success: bool
    msg: str


def save_signature(
    sig_data: str, last_name: str, first_name: str, root_path: Path
) -> SaveResult:
    try:
        save_path = root_path / "output"
        save_path.mkdir(parents=True, exist_ok=True)
        date = datetime.today().strftime("%Y%m%d")
        file_path = save_path / f"{date}_{last_name}_{first_name}.jpg"
        image = Image.open(BytesIO(base64.b64decode(sig_data)))
        image.save(file_path)
        log.info(load_i18n.t("str.msg_signature_saved", locale="en"))
        return SaveResult(True, i18n.tr.MSG_SIGNATURE_SAVED)
    except Exception as exc:
        log.error(load_i18n.t("str.err_during_sig_saving", locale="en"), exc_info=exc)
        return SaveResult(False, i18n.tr.ERR_DURING_SIG_SAVING)
