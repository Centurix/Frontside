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

    def __init__(self, **kwargs):
        self._dimensions = kwargs.pop('dimensions', (100, 100))
        self._states = {
            'up': {
                'background_color': kwargs.pop('up_background_color', (255, 255, 255)),
                'foreground_color': kwargs.pop('up_foreground_color', (0, 0, 0))
            },
            'down': {
                'background_color': kwargs.pop('down_background_color', (255, 0, 0)),
                'foreground_color': kwargs.pop('down_foreground_color', (255, 255, 255))
            }
        }
        self._state = self.up
        self._text = kwargs.pop('text', 'Button')
        self._position = kwargs.pop('position', (1, 1))
        super(self.__class__, self).__init__(kwargs.pop('focused', False))

    def draw(self, canvas):
        """
        * Can draw itself onto a canvas
        * Responds to events
        * Changes display depending on state
        * Fires an action
        * Can acquire a focus
        * Can create an image based on a template or spritesheet
        * Has two draw states, up and down
        * Is either a momentary button or a click down/up button

        Create the button with
        button = Button()
        button.on_click = function()
        button.on_down = function()
        button.on_up = function()
        button.focus = function()
        button.blur = function()

        or

        button = Button(function())

        We need a position, dimensions, image, state
        :param canvas:
        :return:
        """
        surface = pygame.Surface(self._dimensions)
        surface.fill(self._states[self._state]['background_color'])

        font = pygame.font.Font(None, 18)
        text = font.render(self._text, 1, self._states[self._state]['foreground_color'])
        surface.blit(text, (0, 0))

        canvas.blit(surface, self._position)

    def process_event(self, event):
        if not self.focused:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self._state = self.down
                return True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self._state = self.up
                return True
