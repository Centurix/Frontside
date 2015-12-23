# -*- coding: utf-8 -*-
import optparse
import logging


class OptionsParser(object):
    LOG_LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    @staticmethod
    def parse(description, version):
        # Parse command line options
        parser = optparse.OptionParser(
            usage='usage: %prog [options] file\n' + description,
            version='%prog ' + version
        )

        parser.add_option(
            '-l',
            '--log',
            dest='log_file',
            default='./frontside.log',
            help='specify the log file location'
        )
        parser.add_option(
            '-L',
            '--log_level',
            dest='log_level',
            default='info',
            help='specify the log level (%s)' % ', '.join(key for key in OptionsParser.LOG_LEVELS))

        (options, args) = parser.parse_args()

        return options
