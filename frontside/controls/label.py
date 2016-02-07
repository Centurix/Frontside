# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
import pygame


class Label(Control):

    def __init__(self, options):
        default = {
            'theme': 'default',
            'focused': False,
            'dimensions': (2, 1),
            'background_color': (0, 0, 0),
            'foreground_color': (255, 255, 255),
            'text': 'Label',
            'position': (1, 1)
        }
        super(self.__class__, self).__init__(default, options)

    def draw(self, canvas, screen_info):
        """
        * Can create an image based on a template or spritesheet
        * Is either a momentary button or a click down/up button

        :param canvas:
        :param screen_info:
        :return:
        """
        scaler = Scaler(screen_info)

        surface = pygame.Surface(scaler.scale(self._options['dimensions']))
        surface.fill(self._options['background_color'])

        font = pygame.font.Font(None, 18)
        text = font.render(self._options['text'], True, self._options['foreground_color'])
        text_rect = text.get_rect()
        text_rect.centerx = surface.get_rect().centerx
        text_rect.centery = surface.get_rect().centery
        surface.blit(text, text_rect)

        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        # if not self.focused:
        #     return False

        return False, '', {}
