# -*- conding: utf8 -*-

"""
@author: Muhammed Zeba (parice02)
"""

from pathlib import Path
import json
from gettext import gettext as _


def N_(s):
    return s


def load_config():
    CONFIG_FILE = "config/config.json"

    config_file = Path(CONFIG_FILE)
    if config_file.exists() and config_file.is_file():
        with open(file=CONFIG_FILE, mode="r", encoding="utf8") as file:
            return json.load(file)
    raise FileNotFoundError


def load_license():
    LICENCE_FILE = "LICENSE"
    licence_path = Path(LICENCE_FILE)
    if licence_path.exists() and licence_path.is_file():
        with open(file=licence_path, mode="r", encoding="utf8") as file:
            return file.read()
    raise FileNotFoundError


_config = load_config()
