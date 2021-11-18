
import logging
from logging import config as logging_config

from /.log_configuration import log_config


try:
    logging_config.dictConfig(log_config)
except Exception as e:
    raise


if __name__ == '__main__':
    logger = logging.getLogger("LOGGER")
    #logger.info("TEST")
    logger.error("ERROR")
    #print("test")