#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import logging

__description__ = ''
__author__ = 'Chris Read'
__version__ = '0.0.1'
__date__ = '2015/12/16'

"""
FRONTSIDE
=========

MAME frontend using Python and PyGame. Frame buffer friendly.

"""

EXIT_OK = 0
EXIT_OTHER_ERROR = 1
EXIT_PARAM_ERROR = 2

logging.basicConfig()
log = logging.getLogger('frontside')
log.info('Starting frontside')


def main():
    return EXIT_OK


if __name__ == '__main__':
    sys.exit(main())
