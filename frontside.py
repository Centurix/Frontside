#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
from frontside import OptionsParser

__description__ = 'Frontside. M.A.M.E. Front end written in Python using pyGame. Good for frame buffers.'
__author__ = 'Chris Read'
__version__ = '0.0.1'
__date__ = '2015/12/23'

"""
FRONTSIDE
=========
MAME frontend using Python and PyGame. Frame buffer friendly.
"""

EXIT_OK = 0
EXIT_OTHER_ERROR = 1
EXIT_PARAM_ERROR = 2


def main():
    options = OptionsParser.parse(__description__, __version__)
    if options.log_level not in OptionsParser.LOG_LEVELS:
        print('Not a valid log level')
        return EXIT_PARAM_ERROR

    logging.basicConfig(filename=options.log_file, level=OptionsParser.LOG_LEVELS[options.log_level])
    logging.info('Entering frontside')

    return EXIT_OK

if __name__ == '__main__':
    sys.exit(main())
