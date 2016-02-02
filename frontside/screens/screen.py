# -*- coding: utf-8 -*-
import abc
import pygame
from ..theme import Theme
from ..factories import Control
# from ..controls import Button
# from ..controls import Container
# from ..controls import List


class Screen(object):
    """
    Abstract class for a basic screen, make sure __init__ is called
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, config):
        self._config = config
        self._screen_def = 'blank'
        self._controls = []
        self._columns = 12
        self._rows = 12

    def build_controls(self, screen_width, screen_height):
        """
        Build the screen controls from the theme
        :return:
        """
        theme = Theme(self._config['frontside']['theme'])

        self._columns = theme[self._screen_def]['columns']
        self._rows = theme[self._screen_def]['rows']

        column_pixels = int(float(screen_width) / self._columns)
        row_pixels = int(float(screen_height) / self._rows)

        focus = True
        for control in theme[self._screen_def]['controls']:
            self._controls.append(
                Control.factory(control['type'], {
                    'dimensions': (control['width'] * column_pixels, control['height'] * row_pixels),
                    'position': (control['left'] * column_pixels, control['top'] * row_pixels)  # ,
                    # 'background_color': (128, 128, 128),
                    # 'foreground_color': (0, 0, 0),
                    # 'text': control['text'] if control['text'] else '',
                    # 'focused': focus,
                    # 'key': control['key'],
                    # 'key_up': control['key_up']
                })
            )

            # if control['type'] == 'button':
            #     self._controls.append(Button({
            #         'dimensions': (control['width'] * column_pixels, control['height'] * row_pixels),
            #         'background_color': (128, 128, 128),
            #         'foreground_color': (0, 0, 0),
            #         'text': control['text'],
            #         'focused': focus,
            #         'position': (control['left'] * column_pixels, control['top'] * row_pixels),
            #         'key': control['key'],
            #         'key_up': control['key_up']
            #     }))
            #     focus = False
            # elif control['type'] == 'container':
            #     self._controls.append(Container({
            #         'dimensions': (control['width'] * column_pixels, control['height'] * row_pixels),
            #         'position': (control['left'] * column_pixels, control['top'] * row_pixels)
            #     }))
            # elif control['type'] == 'list':
            #     self._controls.append(List({
            #         'dimensions': (control['width'] * column_pixels, control['height'] * row_pixels),
            #         'position': (control['left'] * column_pixels, control['top'] * row_pixels)
            #     }))

    def show(self):
        """
        Do we do pygame.init() for every screen?
        :return:
        """

        width = self._config['frontside']['width']
        height = self._config['frontside']['height']

        self.build_controls(width, height)

        pygame.init()
        screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

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

    def render(self, canvas):
        for control in self._controls:
            control.draw(canvas)
