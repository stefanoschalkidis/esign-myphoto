import i18n


class Translations:
    def __init__(self):
        self.MSG_CONFIG_FILE_NOT_FOUND = i18n.t("str.msg_config_file_not_found")


tr: Translations = Translations()


def initialize() -> None:
    global tr
    tr = Translations()
