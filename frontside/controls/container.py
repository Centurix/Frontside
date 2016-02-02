# -*- coding: utf-8 -*-
from control import Control
import pygame


class Container(Control):
    def __init__(self, options):
        default = {
            'dimensions': (100, 100),
            'position': (1, 1)
        }
        self._options = dict(default.items() + options.items())
        super(self.__class__, self).__init__(False)

    def draw(self, canvas):
        surface = pygame.Surface(self._options['dimensions'])
        surface.fill((255, 255, 255))

        """
        Render any children controls
        """

        canvas.blit(surface, self._options['position'])

    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        return False, '', {}
