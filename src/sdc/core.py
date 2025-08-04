import logging

import seppl


ENV_SDC_LOGLEVEL = "SDC_LOGLEVEL"
""" environment variable for the global default logging level. """


class Session(seppl.Session):
    """
    Session object shared among reader, filter(s), writer.
    """
    logger: logging.Logger = logging.getLogger("spectral-data-converter")
    """ the global logger. """
