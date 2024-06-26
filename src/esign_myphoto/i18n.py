import i18n


class Translations:
    def __init__(self, lang_code="en"):
        self.LANG_CODE = lang_code

        self.BUTTON_CAPTURE_SIGNATURE = i18n.t("str.button_capture_signature")
        self.BUTTON_HOME = i18n.t("str.button_home")

        self.ERR_DURING_SIG_SAVING = i18n.t("str.err_during_sig_saving")
        self.ERR_INITIALIZATION = i18n.t("str.err_initialization")
        self.ERR_LICENSE_OR_REASON_NOT_DEFINED = i18n.t(
            "str.err_license_or_reason_not_defined"
        )
        self.ERR_NO_DIGITIZER_CONNECTED = i18n.t("str.err_no_digitizer_connected")
        self.ERR_WACOM_SDK_NOT_LICENSED = i18n.t("str.err_wacom_sdk_not_licensed")

        self.LABEL_FIRST_NAME = i18n.t("str.label_first_name")
        self.LABEL_LAST_NAME = i18n.t("str.label_last_name")

        self.MSG_CAPTURE_FAILED = i18n.t("str.msg_capture_failed")
        self.MSG_CAPTURE_SUCCESSFUL = i18n.t("str.msg_capture_successful")
        self.MSG_CAPTURED_SIGNATURE = i18n.t("str.msg_captured_signature")
        self.MSG_CAPTURING_SIGNATURE = i18n.t("str.msg_capturing_signature")
        self.MSG_CONFIG_FILE_NOT_FOUND = i18n.t("str.msg_config_file_not_found")
        self.MSG_INVALID_CHARACTER_ENTERED = i18n.t("str.msg_invalid_character_entered")
        self.MSG_PLEASE_COMPLETE_ALL_FIELDS = i18n.t(
            "str.msg_please_complete_all_fields"
        )
        self.MSG_SIG_CAPTURE_CANCELLED = i18n.t("str.msg_sig_capture_cancelled")
        self.MSG_SIG_TABLE_MISSING = i18n.t("str.msg_sig_table_missing")
        self.MSG_SIGNATURE_SAVED = i18n.t("str.msg_signature_saved")
        self.MSG_WACOM_DRIVER_NOT_INSTALLED = i18n.t(
            "str.msg_wacom_driver_not_installed"
        )
        self.MSG_WACOM_SDK_NOT_INSTALLED = i18n.t("str.msg_wacom_sdk_not_installed")

        self.TITLE_INFORMATION = i18n.t("str.title_information")


tr: Translations = Translations()


def initialize(lang_code: str) -> None:
    global tr
    tr = Translations(lang_code)
