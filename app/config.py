"""
Handles Environmental Configuration 
Logging settings
"""

# Import necessary modules
import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
import os
import sys

# Define the root directory of the package
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Define the log format
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s -"
    "%(funcName)s:%(lineno)d - %(message)s"
)

# Define the directory for log files
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'ml_api.log'


def get_console_handler():
    """Configure console logging handler"""
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    """Configure file logging handler"""
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight'
    )
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    """Get logger with prepared handlers"""

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


class Config:
    """Base configuration class"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-need-to-be-changed'
    SERVER_PORT = 5000


class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT', 5000)

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
