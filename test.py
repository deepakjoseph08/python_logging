import os
import logging


from logging import config as logging_config

log_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "%(asctime)s : %(name)s : %(levelname)s : %(message)s "
        },
        "error": {"format": "%(asctime)s : %(name)s : %(levelname)s : %(message)s : %(module)s : %(filename)s "
                  }

    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "console_2": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "error",
            "stream": "ext://sys.stdout"
        },

        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "error",
            "filename": "logs/INFO/info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "schedule_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "error",
            "filename": "logs/INFO/scheduler.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },

        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "error",
            "filename": "logs/ERROR/errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },

    "loggers": {
        "LOGGER": {
            "level": "DEBUG",
            "handlers": ["console", "error_file_handler", "info_file_handler", "console_2"],
            "propagate": "no"
        },
        "schedule": {
            "level": "DEBUG",
            "handlers": ["schedule_handler", "error_file_handler", "info_file_handler", "console_2"],
            "propagate": "no"

        }
    }

}


log_info_directory = 'logs/INFO'
log_error_directory = "logs/ERROR"

try:
    if not os.path.exists(log_info_directory):
        os.makedirs(log_info_directory)
    if not os.path.exists(log_error_directory):
        os.makedirs(log_error_directory)
except OSError, e:
    raise Exception(e)
    # print("COntinues safe")
# os.makedirs(log_error_directory)
# with open(log_config, 'r') as f:
#     config = json.load(f)
#     #print(config)
try:
    logging_config.dictConfig(log_config)
except Exception as e:
    raise

if __name__ == '__main__':
    logger = logging.getLogger("LOGGER")
    logger.info("TEST")
    print("test")