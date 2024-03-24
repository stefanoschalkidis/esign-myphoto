import logging
import sys
from pathlib import Path

from esign_myphoto import io as app_io

log_format = "[%(levelname)s] - %(message)s"
handlers = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(level=logging.INFO, format=log_format, handlers=handlers)

root_path = Path(__file__).parent.parent

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    root_path = Path(sys.executable).parent

if __name__ == "__main__":
    sig_config = app_io.load_sig_config(root_path / "config/config.toml")
