# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
import pygame


class Text(Control):
    def __init__(self, options):
        default = {
            'dimensions': (100, 100),
            'position': (1, 1),
            'focused': False
        }
        super(self.__class__, self).__init__(default, options)

    def draw(self, canvas, screen_info):
        scaler = Scaler(screen_info)
        surface = pygame.Surface(scaler.scale(self._options['dimensions']))
        surface.fill((255, 128, 128))


        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        return False, '', {}
