#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
from frontside import OptionsParser
from frontside import ConfigParser
from frontside import Frontside


__description__ = 'Frontside. M.A.M.E. Front end using pyGame. Good for frame buffers.'
__author__ = 'Chris Read'
__version__ = '0.0.1'
__date__ = '2016/01/17'

"""
FRONTSIDE
=========
MAME frontend using Python and PyGame. Frame buffer friendly.
"""

EXIT_OK = 0
EXIT_OTHER_ERROR = 1
EXIT_PARAM_ERROR = 2


def main():
    """
    Deal with startup config, merge file config and priority command line options. Respect the command line.
    :return: Provide the proper exit code
    """
    options = OptionsParser.parse(__description__, __version__)
    if options['log_level'] not in OptionsParser.LOG_LEVELS:
        print('Not a valid log level')
        return EXIT_PARAM_ERROR

    config, results = ConfigParser.parse(options['config_file'])
    if type(results) is dict:
        ConfigParser.display_errors(config, results)
        return EXIT_PARAM_ERROR

    for key in options:
        if key != 'config_file':
            config['frontside'][key] = options[key]

    # Merge options and config
    logging.basicConfig(
        filename=config['frontside']['log_file'],
        level=OptionsParser.LOG_LEVELS[config['frontside']['log_level']]
    )
    logging.info('Entering frontside')

    application = Frontside(config)
    application.start()
    return EXIT_OK

if __name__ == '__main__':
    sys.exit(main())
