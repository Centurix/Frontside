# -*- coding: utf-8 -*-


class Scaler(object):
    def __init__(self, screen_info):
        self._screen_info = screen_info

    def scale(self, (dx, dy)):
        return dx * self._screen_info['pixels_per_column'], dy * self._screen_info['pixels_per_row']
