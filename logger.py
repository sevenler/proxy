import logging
LOGGER = {
    'TITLE': "Crowdsourcing",
    'LEVEL': logging.DEBUG,
    'FORMAT': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}

__all__ = ['logger']

#logging.basicConfig(format=LOGGER['format'], datefmt=LOGGER['datefmt'])
logger = logging.getLogger(LOGGER['TITLE'])
logger.setLevel(LOGGER['LEVEL'])

#TODO add file handler
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter(LOGGER['FORMAT'])
# add formatter to ch
ch.setFormatter(formatter)
logger.addHandler(ch)
