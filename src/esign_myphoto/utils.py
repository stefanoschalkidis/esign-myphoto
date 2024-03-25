import logging as log
import windows_tools.installed_software as wintools

from esign_myphoto import i18n


def are_wacom_deps_met() -> bool:
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
        log.error(i18n.tr.MSG_WACOM_SDK_NOT_INSTALLED)
        return False

    if not has_stu and not has_tablet:
        log.error(i18n.tr.MSG_WACOM_DRIVER_NOT_INSTALLED)
        return False

    return True
