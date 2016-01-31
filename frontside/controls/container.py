# -*- coding: utf-8 -*-
from control import Control
import pygame


class Container(Control):
    def __init__(self, **kwargs):
        self._dimensions = kwargs.pop('dimensions', (100, 100))
        self._position = kwargs.pop('position', (1, 1))
        super(self.__class__, self).__init__(False)

    def draw(self, canvas):
        surface = pygame.Surface(self._dimensions)
        surface.fill((255, 255, 255))

        canvas.blit(surface, self._position)

    def process_event(self, event):
        if not self.focused:
            return False
