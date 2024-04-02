import logging as log
import sys
from dataclasses import dataclass

import i18n as load_i18n

if sys.platform.startswith("win"):
    import windows_tools.installed_software as wintools

from esign_myphoto import i18n


def is_windows():
    return sys.platform.startswith("win")


@dataclass
class WacomDepsCheckResult:
    success: bool
    msg: str | None


def check_wacom_deps() -> WacomDepsCheckResult:
    programs = wintools.get_installed_software()
    has_sdk = False
    has_stu = False
    has_tablet = False

    for program in programs:
        name = program["name"]

        if name == "Wacom Signature SDK":
            has_sdk = True

        if name == "Wacom STU Driver (x64)":
            has_stu = True

        if name == "Wacom Tablet":
            has_tablet = True

    if not has_sdk:
        lang_key = "str.msg_wacom_sdk_not_installed"
        log.error(load_i18n.t(lang_key, locale="en"))
        return WacomDepsCheckResult(False, i18n.tr.MSG_WACOM_SDK_NOT_INSTALLED)

    if not has_stu and not has_tablet:
        lang_key = "str.msg_wacom_driver_not_installed"
        log.error(load_i18n.t(lang_key, locale="en"))
        return WacomDepsCheckResult(False, i18n.tr.MSG_WACOM_DRIVER_NOT_INSTALLED)

    return WacomDepsCheckResult(True, None)
