# -*- coding: utf-8 -*-
import abc
import pygame
from ..theme import Theme
from ..factories import Control


class Screen(object):
    """
    Abstract class for a basic screen, make sure __init__ is called
    """
    __metaclass__ = abc.ABCMeta

    _screen_def = 'blank'

    def __init__(self, config):
        self._controls = []
        self._config = config
        self._theme = Theme(self._config['frontside']['theme'])

        width = self._config['frontside']['width']
        height = self._config['frontside']['height']

        columns = self._theme[self._screen_def]['columns']
        rows = self._theme[self._screen_def]['rows']

        self._screen_info = {
            'pixels_per_column': int(float(width) / columns),
            'pixels_per_row': int(float(height) / rows)
        }

    def build_controls(self):
        """
        Build the screen controls from the theme
        :return:
        """
        for control in self._theme[self._screen_def]['controls']:
            self._controls.append(Control.factory(control['type'], control))

    def show(self):
        """
        Do we do pygame.init() for every screen?
        :return:
        """
        self.build_controls()

        pygame.init()
        screen = pygame.display.set_mode((self._config['frontside']['width'], self._config['frontside']['height']), pygame.DOUBLEBUF)

        clock = pygame.time.Clock()
        complete = False
        while not complete:
            clock.tick(60)
            for event in pygame.event.get():
                """
                Handle all the base events that should not be handled by any controls
                pygame.QUIT, CTRL+w, ALT+F4, ESCAPE
                """
                if event.type == pygame.QUIT:
                    complete = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL) or \
                       (event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT) or \
                       (event.key == pygame.K_ESCAPE):
                        complete = True

                # Now process the event through each control on the screen
                for control in self._controls:
                    processed, trigger, params = control.process_event(event)
                    if processed:
                        if trigger != '':
                            for method in dir(self):
                                attr = getattr(self, method)
                                if callable(attr) and method == trigger:
                                    attr(params)
                        break

            self.render(screen)
            pygame.display.flip()

        screen.fill((0, 0, 0))

    def render(self, canvas):
        for control in self._controls:
            control.draw(canvas, self._screen_info)
