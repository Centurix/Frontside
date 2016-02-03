# -*- coding: utf-8 -*-
from screen import Screen


class JoystickTest(Screen):
    _screen_def = 'joystick_test'

    def __init__(self, config):
        super(self.__class__, self).__init__(config)
