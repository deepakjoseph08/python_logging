
log_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "%(asctime)s : %(name)s : %(levelname)s : %(message)s"
        },
        "error": {"format":  "%(asctime)s : %(name)s : %(levelname)s : %(message)s : %(module)s : %(filename)s"
                  }

    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "error",
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
            "filename": "info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "schedule_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "error",
            "filename": "scheduler.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },

        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "error",
            "filename": "errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },

    "loggers": {
        "LOGGER": {
            "level": "DEBUG",
            "handlers": ["console", "error_file_handler", "info_file_handler"],
            "propagate": "no"
        },
        "schedule": {
            "level": "DEBUG",
            "handlers": ["schedule_handler", "error_file_handler", "info_file_handler", "console_2"],
            "propagate": "no"

        }
    }

}