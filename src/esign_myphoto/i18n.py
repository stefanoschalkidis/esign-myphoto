import i18n


class Translations:
    def __init__(self):
        self.ERR_SIGNATURE_CAPTURE = i18n.t("str.err_signature_capture")

        self.MSG_CAPTURING_SIGNATURE = i18n.t("str.msg_capturing_signature")
        self.MSG_CONFIG_FILE_NOT_FOUND = i18n.t("str.msg_config_file_not_found")
        self.MSG_INVALID_CHARACTER_ENTERED = i18n.t("str.msg_invalid_character_entered")
        self.MSG_SIG_TABLE_MISSING = i18n.t("str.msg_sig_table_missing")
        self.MSG_WACOM_DRIVER_NOT_INSTALLED = i18n.t(
            "str.msg_wacom_driver_not_installed"
        )
        self.MSG_WACOM_SDK_NOT_INSTALLED = i18n.t("str.msg_wacom_sdk_not_installed")

        self.QUESTION_ENTER_FIRST_NAME = i18n.t("str.question_enter_first_name")
        self.QUESTION_ENTER_LAST_NAME = i18n.t("str.question_enter_last_name")


tr: Translations = Translations()


def initialize() -> None:
    global tr
    tr = Translations()
