# -*- conding: utf8 -*-

"""
@author: Muhammed Zeba (parice02)
"""

import time
import sqlite3
from re import compile, I
from typing import List
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


class Timer(object):
    """ """

    def __enter__(self):
        self.start()
        # __enter__ must return an instance bound with the "as" keyword
        return self

    def __exit__(self, *args, **kwargs):
        # There are other arguments to __exit__ but we don't care here
        self.stop()

    def start(self):
        if hasattr(self, "interval"):
            del self.interval
        self.start_time = time.time()

    def stop(self):
        if hasattr(self, "start_time"):
            self.interval = time.time() - self.start_time
            del self.start_time  # Force timer re-init


class LoggerTimer(Timer):
    """
    Source: https://saladtomatonion.com/blog/2014/12/16/mesurer-le-temps-dexecution-de-code-en-python/
    """

    @staticmethod
    def default_logger(msg):
        print(msg)

    def __init__(self, prefix="", func=None):
        # Use func if not None else the default one
        self.f = func or LoggerTimer.default_logger
        # Format the prefix if not None or empty, else use empty string
        self.prefix = f"{prefix}" if prefix else ""

    def __call__(self, func):
        # Use self as context manager in a decorated function
        def decorated_func(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return decorated_func

    def stop(self):
        # Call the parent method
        super(LoggerTimer, self).stop()
        # Call the logging function with the message
        self.f(f"{self.prefix}: {self.interval}")


class DBSQLite3(object):
    """ """

    def __init__(self, sqlite3_db: str = "db.db"):
        """ """
        self._connection = sqlite3.connect(sqlite3_db)
        self._connection.create_function("regexp", 2, regexp)
        self._cursor = self._connection.cursor()

    def close_connection(self):
        """ """
        self._connection.close()

    def close_cursor(self):
        """ """
        self._cursor.close()

    @LoggerTimer("DBSQLite.execute_query() process time")
    def execute_query(self, params) -> List:
        """ """
        query = "SELECT DISTINCT mot FROM mots WHERE LENGTH(mot) = :len AND regexp(:expr, mot)"
        try:
            self._cursor.execute(query, params)
            results = listfetchall(self._cursor)
            return (
                results
                if len(results) != 0
                else [
                    0,
                    _("Aucune correspondance trouvée"),
                ]
            )
        except Exception as e:
            return [
                0,
                e.__str__(),
            ]


_config = load_config()
