import logging
import modules.config


def setup_logger():
    logging.basicConfig(
        level=modules.config.LOGGING_LEVEL,
        format=modules.config.LOGGING_FORMAT,
        datefmt=modules.config.LOGGING_DATEFMT,
    )
    return logging.getLogger(__name__)


logger = setup_logger()
