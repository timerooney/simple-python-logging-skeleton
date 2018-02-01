import logging
LOGGER = logging.getLogger(__name__)

def print_something():
    LOGGER.info('Printing from the second module')
    print('This is the second module')
