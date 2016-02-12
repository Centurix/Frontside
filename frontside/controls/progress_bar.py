# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
import pygame


class ProgressBar(Control):
    def __init__(self, options):
        default = {
            'theme': 'default',
            'focused': False,
            'dimensions': (2, 1),
            'background_color': (128, 128, 128),
            'foreground_color': (0, 0, 0),
            'text': 'Button',
            'position': (1, 1)
        }
        self._current = 0
        self._total = 1
        super(self.__class__, self).__init__(default, options)

    def set_total(self, total):
        self._total = total

    def set_current(self, current):
        self._current = current

    def set_text(self, text):
        self._options['text'] = text

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

        percent = float(self._current) / self._total * 100

        width, height = scaler.scale(self._options['dimensions'])
        width = int(float(width) / 100 * percent)

        progress_bar_surface = pygame.Surface((width, height))
        progress_bar_surface.fill((0, 0, 128))

        progress_bar_rect = progress_bar_surface.get_rect()

        surface.blit(progress_bar_surface, progress_bar_rect)

        font = pygame.font.Font(None, 18)
        text = font.render("%s (%d%%)" % (self._options['text'], percent), True, self._options['foreground_color'])
        text_rect = text.get_rect()
        text_rect.centerx = surface.get_rect().centerx
        text_rect.centery = surface.get_rect().centery
        surface.blit(text, text_rect)

        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        return False, '', {}
