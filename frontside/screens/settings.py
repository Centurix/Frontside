# -*- coding: utf-8 -*-
from screen import Screen
from ..mame import Mame
# from ..repositories import RomRepository
from ..scanner import Scanner
import sys
import time


class Settings(Screen):
    _screen_def = 'settings'

    def __init__(self, config, connection):
        super(self.__class__, self).__init__(config, connection)

    def start_scanner(self, params):
        print "Starting the scanner"
        scanner = Scanner(self._config)
        scanner.register_observer(self)
        scanner.start()

    def redefine_keys(self, params):
        print "Redefining the keys"
        # TODO: Redefine some key

    def notify(self, observable, current_line, line_count):
        percent = float(current_line) / line_count * 100
        done = ('#' * int(float(50) / 100 * percent)) + ('-' * 50)
        sys.stdout.write('\r|%s| (%.2f%%)' % (done[:50], percent))
        sys.stdout.flush()

        time.sleep(.000001)
