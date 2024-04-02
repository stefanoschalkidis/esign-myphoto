import ctypes
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

import i18n as load_i18n

from esign_myphoto import io as app_io, i18n, utils
from esign_myphoto.gui import App

ctypes.windll.shcore.SetProcessDpiAwareness(1)

data_path = Path(__file__).parent / "data"
root_path = Path(__file__).parent.parent

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    root_path = Path(sys.executable).parent

os.makedirs(root_path / "logs", exist_ok=True)
log_format = "[%(asctime)s] [%(levelname)s] - %(message)s"
log_file_handler = RotatingFileHandler(
    "logs/amy_e-sign_myphoto.log",
    mode="a",
    maxBytes=5000000,
    backupCount=2,
    encoding="utf-8",
)
handlers = (log_file_handler,)
logging.basicConfig(level=logging.INFO, format=log_format, handlers=handlers)  # NOSONAR

if __name__ == "__main__":
    config_file = root_path / "config/config.toml"
    lang_code = app_io.load_lang_code(config_file)
    load_i18n.load_path.append(str(data_path / "i18n"))
    load_i18n.set("locale", lang_code)
    i18n.initialize(lang_code)
    init_err = None

    load_result = app_io.load_sig_config(config_file)

    if (
        not load_result.sig_config.license or not load_result.sig_config.reason
    ) and load_result.msg:
        init_err = load_result.msg

    deps_check = utils.check_wacom_deps()

    if not deps_check.success and deps_check.msg:
        init_err = deps_check.msg

    app = App(init_err, root_path, data_path, load_result.sig_config)
    app.mainloop()
