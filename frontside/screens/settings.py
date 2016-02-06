# -*- coding: utf-8 -*-
from screen import Screen


class Settings(Screen):
    _screen_def = 'settings'

    def __init__(self, config):
        super(self.__class__, self).__init__(config)

    def start_scanner(self, params):
        print "Starting the scanner"

    def redefine_keys(self, params):
        print "Redefining the keys"
