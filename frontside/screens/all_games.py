# -*- coding: utf-8 -*-
from screen import Screen
from settings import Settings
from joystick_test import JoystickTest
from ..mame.mame import Mame
from ..list_providers import RomProvider


class AllGames(Screen):
    _screen_def = 'all_games'

    def __init__(self, config, connection):
        super(self.__class__, self).__init__(config, connection)
        self.find_control('gamelist').set_list(RomProvider(self._connection))

    def start_game(self, params):
        """
        Get the currently selected game and play it
        :param params:
        :return:
        """
        Mame(self._config).play('pengo')

    def settings(self, params):
        settings = Settings(self._config, self._connection)
        settings.show()

    def joystick_test(self, params):
        joystick_test = JoystickTest(self._config, self._connection)
        joystick_test.show()
