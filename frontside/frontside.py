# -*- coding: utf-8 -*-
from mame import Mame
from configobj import ConfigObj
from validate import Validator


class Frontside(object):
    def __init__(self, options):
        print(options)
        pass

    def start(self):
        vdt = Validator()
        vdt.check('integer', 10, 10)
        config = ConfigObj(
            configspec='./default.ini',
            infile='./frontside.ini',
            create_empty=True,
            file_error=False,
            encoding='UTF-8'
        )
        config.validate(vdt, copy=True)
        config.write()
#        mame = Mame(config)
        pass
