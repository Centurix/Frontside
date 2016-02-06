# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
import pygame


class Button(Control):
    @property
    def up(self):
        return 'up'

    @property
    def down(self):
        return 'down'

    @property
    def disabled(self):
        return 'disabled'

    def __init__(self, options):
        default = {
            'theme': 'default',
            'focused': False,
            'dimensions': (2, 1),
            'background_color': (128, 128, 128),
            'foreground_color': (0, 0, 0),
            'text': 'Button',
            'focused': False,
            'position': (1, 1),
            'key': '',
            'key_up': '',
            'key_down': '',
            'focus': '',
            'blur': '',
            'states': {
                'up': {
                    'background_color': (255, 255, 255),
                    'foreground_color': (0, 0, 0)
                },
                'down': {
                    'background_color': (255, 0, 0),
                    'foreground_color': (255, 255, 255)
                },
                'disabled': {
                    'background-color': (0, 0, 0),
                    'foreground-color': (80, 80, 80)
                }
            }
        }
        self._state = self.up
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
        surface.fill(self._options['states'][self._state]['background_color'])

        font = pygame.font.Font(None, 18)
        text = font.render(self._options['text'], True, self._options['states'][self._state]['foreground_color'])
        text_rect = text.get_rect()
        text_rect.centerx = surface.get_rect().centerx
        text_rect.centery = surface.get_rect().centery
        surface.blit(text, text_rect)

        canvas.blit(surface, scaler.scale(self._options['position']))

    def process_event(self, event):
        # if not self.focused:
        #     return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == self._options['key']:
                self._state = self.down
                return True, self._options['key_down'], {}
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN or event.key == self._options['key']:
                self._state = self.up
                return True, self._options['key_up'], {}

        return False, '', {}
