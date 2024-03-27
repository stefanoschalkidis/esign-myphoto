import logging
import sys
from pathlib import Path

import i18n as load_i18n

from esign_myphoto import io as app_io, i18n, utils, sig

log_format = "[%(levelname)s] %(message)s"
handlers = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(level=logging.INFO, format=log_format, handlers=handlers)

data_path = Path(__file__).parent / "data"
root_path = Path(__file__).parent.parent

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    root_path = Path(sys.executable).parent


def run_app():
    config_file = root_path / "config/config.toml"
    lang_code = app_io.load_lang_code(config_file)
    load_i18n.load_path.append(str(data_path / "i18n"))
    load_i18n.set("locale", lang_code)
    i18n.initialize()

    sig_config = app_io.load_sig_config(config_file)

    if not sig_config:
        logging.error(i18n.tr.ERR_LICENSE_OR_REASON_NOT_DEFINED)
        return

    if not utils.are_wacom_deps_met():
        return

    logging.info(i18n.tr.MSG_WELCOME_TO_ESIGN_MYPHOTO)
    signer = app_io.prompt_for_signer()
    sig_data = sig.capture_signature(sig_config, lang_code, signer)

    if not sig_data:
        return

    app_io.save_signature(sig_data, signer, root_path)


if __name__ == "__main__":
    run_app()

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        input(i18n.tr.MSG_PRESS_ENTER_TO_CLOSE)
