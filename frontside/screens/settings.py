# -*- coding: utf-8 -*-
from screen import Screen
from ..scanner import Scanner
from ..global_objects import GlobalObjects


class Settings(Screen):
    _screen_def = 'settings'

    def __init__(self, config, connection):
        super(self.__class__, self).__init__(config, connection)

    def start_scanner(self, params):
        GlobalObjects.scanner = Scanner(self._config)
        GlobalObjects.scanner.register_observer(self)
        GlobalObjects.scanner.start()

    def redefine_keys(self, params):
        print "Redefining the keys"
        # TODO: Redefine some key

    def notify(self, observable, current_line, line_count):
        progress_bar = self.find_control('rom_progress')
        progress_bar.set_total(line_count)
        progress_bar.set_current(current_line)
