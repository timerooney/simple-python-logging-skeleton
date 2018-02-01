import logging
LOGGER = logging.getLogger(__name__)

def print_something():
    LOGGER.info('Printing from the first module')
    print('This is the first module')
