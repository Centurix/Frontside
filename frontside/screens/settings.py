# -*- coding: utf-8 -*-
from screen import Screen


class Settings(Screen):
    _screen_def = 'settings'

    def __init__(self, config, connection):
        super(self.__class__, self).__init__(config, connection)

    def start_scanner(self, params):
        print "Starting the scanner"
        # TODO: Start the scanner thread

    def redefine_keys(self, params):
        print "Redefining the keys"
        # TODO: Redefine some key
