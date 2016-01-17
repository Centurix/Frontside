# -*- coding: utf-8 -*-
from configobj import ConfigObj, flatten_errors
from validate import Validator


class ConfigParser(object):
    @staticmethod
    def parse(filename='./frontside.ini'):
        config = ConfigObj(
            configspec='./configspec.ini',
            infile=filename,
            create_empty=True,
            file_error=False,
            encoding='UTF-8'
        )
        results = config.validate(Validator(), copy=True, preserve_errors=True)
        return config, results

    @staticmethod
    def display_errors(config, results):
        for section_list, key, error in flatten_errors(config, results):
            if key is None:
                print('Missing section [%s]' % (', '.join(section_list)))
            else:
                print('Config problem in section [%s], with key %s: %s' % (', '.join(section_list), key, error))
