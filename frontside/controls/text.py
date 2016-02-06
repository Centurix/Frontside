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

        # Draw any existing text
        # Pop open an on screen keyboard where needed
        # 1 2 3 4 5 6 7 8 9 0
        # Q W E R T Y U I O P
        # A S D F G H J K L
        # ^ Z X C V B N M
        #       SPACE

        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        return False, '', {}
