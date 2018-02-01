"""A simple module that handles loading and configuring of the logging system"""
import os
import logging
import logging.config

# Logging configuration
LOGGING_CONFIG_PATH = '%s\\logging.conf' % os.path.dirname(__file__)
LOGGING_FILE = 'run.log'
logging.config.fileConfig(LOGGING_CONFIG_PATH,
                          defaults={'logfilename': LOGGING_FILE})
logging.debug('Logging configuration from %s loaded', LOGGING_CONFIG_PATH)
