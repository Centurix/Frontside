# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
import pygame


class List(Control):
    """
    This needs to have a data source and also react to up/down/left/right
    """
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
        surface.fill((255, 255, 255))

        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print "UP"
                return True, '', {}
            elif event.key == pygame.K_DOWN:
                print "DOWN"
                return True, '', {}
            elif event.key == pygame.K_LEFT:
                print "LEFT"
                return True, '', {}
            elif event.key == pygame.K_RIGHT:
                print "RIGHT"
                return True, '', {}

        return False, '', {}
