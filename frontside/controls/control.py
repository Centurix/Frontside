# -*- coding: utf-8 -*-
import abc
from ..theme import Theme

class Control(object):
    """
    Abstract class for a basic model, make sure __init__ is called
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, default, options):
        self._options = dict(default.items() + options.items())

    @property
    def focused(self):
        return self._options['focused']

    @property
    def name(self):
        return self._options['name']

    @abc.abstractmethod
    def draw(self, canvas, screen_info):
        pass

    @abc.abstractmethod
    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        return False, '', {}

    def scale(self, (dx, dy)):
        """
        Scale the dx and dy, return actual pixel sizes
        :return:
        """
        theme = Theme(self._options['current_display']['theme'])

        columns = theme[self._options['current_display']['screen_def']]['columns']
        rows = theme[self._options['current_display']['screen_def']]['rows']

        column_pixels = int(float(self._options['current_display']['screen_dimensions']['width']) / columns)
        row_pixels = int(float(self._options['current_display']['screen_dimensions']['height']) / rows)

        return dx * column_pixels, dy * row_pixels
