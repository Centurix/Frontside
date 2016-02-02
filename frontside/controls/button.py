# -*- coding: utf-8 -*-
from control import Control
import pygame


class Button(Control):
    @property
    def up(self):
        return 'up'

    @property
    def down(self):
        return 'down'

    def __init__(self, options):
        default = {
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
                }
            }
        }
        self._options = dict(default.items() + options.items())
        self._state = self.up
        super(self.__class__, self).__init__(self._options['focused'])

    def draw(self, canvas):
        """
        * Can create an image based on a template or spritesheet
        * Is either a momentary button or a click down/up button

        :param canvas:
        :return:
        """
        surface = pygame.Surface(self._options['dimensions'])
        surface.fill(self._options['states'][self._state]['background_color'])

        font = pygame.font.Font(None, 18)
        text = font.render(self._options['text'], 1, self._options['states'][self._state]['foreground_color'])
        surface.blit(text, (0, 0))

        canvas.blit(surface, self._options['position'])

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
