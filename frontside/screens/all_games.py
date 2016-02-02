# -*- coding: utf-8 -*-
from screen import Screen
from settings import Settings
from ..mame.mame import Mame


class AllGames(Screen):
    def __init__(self, config):
        super(self.__class__, self).__init__(config)
        self._screen_def = 'all_games'

    def start_game(self, params):
        """
        Get the currently selected game and play it
        :param params:
        :return:
        """
        Mame(self._config).play('pengo')

    def settings(self, params):
        Settings(self._config).show()
