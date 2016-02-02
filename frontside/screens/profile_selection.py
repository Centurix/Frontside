# -*- coding: utf-8 -*-
from screen import Screen


class ProfileSelection(Screen):
    def __init__(self, config):
        super(self.__class__, self).__init__(config)
        self._screen_def = 'profile_selection'
