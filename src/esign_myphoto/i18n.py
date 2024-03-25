import i18n


class Translations:
    def __init__(self):
        self.MSG_CONFIG_FILE_NOT_FOUND = i18n.t("str.msg_config_file_not_found")
        self.MSG_SIG_TABLE_MISSING = i18n.t("str.msg_sig_table_missing")
        self.MSG_WACOM_DRIVER_NOT_INSTALLED = i18n.t(
            "str.msg_wacom_driver_not_installed"
        )
        self.MSG_WACOM_SDK_NOT_INSTALLED = i18n.t("str.msg_wacom_sdk_not_installed")


tr: Translations = Translations()


def initialize() -> None:
    global tr
    tr = Translations()
