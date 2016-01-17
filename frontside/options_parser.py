# -*- coding: utf-8 -*-
import argparse
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
        """

        :param description:
        :param version:
        :return:
        """
        parser = argparse.ArgumentParser(
            description=description,
            add_help=True
        )
        parser.add_argument(
            '-l',
            '--log_file',
            dest='log_file',
            help='Log file location',
            default='./frontside.log'
        )
        parser.add_argument(
            '-L',
            '--log_level',
            dest='log_level',
            help='Log level',
            default='info',
            choices=[key for key in OptionsParser.LOG_LEVELS]
        )
        parser.add_argument(
            '-C',
            '--config_file',
            dest='config_file',
            help='Config file location',
            default='./frontside.ini'
        )
        parser.add_argument(
            '-v',
            '--version',
            help='Show the version number',
            action='version',
            version=version
        )
        (options, args) = parser.parse_known_args()

        return vars(options)
