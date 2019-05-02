# coding=utf-8
"""
Provides a common way to initialize a logger.
"""
import os
import sys
import logging as _logging


_LEVELS = {
    "0": _logging.INFO,
    "1": _logging.DEBUG,
    "10": _logging.DEBUG,
    "20": _logging.INFO,
    "INFO": _logging.INFO,
    "DEBUG": _logging.DEBUG,
}


def get_default_formatter() -> _logging.Formatter:
    return _logging.Formatter("[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s")


def get_logger(name: str) -> _logging.Logger:
    """
    Return a logger with the specified name, creating it if necessary.
    Typically called as `get_logger(__name__)`.
    """
    logger = _logging.getLogger(name)
    # only add the typical stderr stream handler once (get_logger could be called multiple times)
    if not any(type(handler) is _logging.StreamHandler and handler.stream == sys.stderr for handler in logger.handlers):
        sh = _logging.StreamHandler()
        sh.setFormatter(get_default_formatter())
        logger.addHandler(sh)
    logger.setLevel(_LEVELS.get(os.environ.get("WORKLOGS_LOG_LEVEL"), _logging.INFO))
    return logger
