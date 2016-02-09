# -*- coding: utf-8 -*-
from control import Control
from ..screens.scaler import Scaler
from ..list_providers import ListProvider
import pygame


class List(Control):
    """
    This needs to have a data source and also react to up/down/left/right
    """
    def __init__(self, options):
        default = {
            'dimensions': (100, 100),
            'position': (1, 1),
            'focused': False,
            'background_color': (0, 0, 0),
            'foreground_color': (0, 0, 0),
            'font_size': 18
        }
        self._list = ListProvider(None)
        self._position = 0
        super(self.__class__, self).__init__(default, options)

    def draw(self, canvas, screen_info):
        scaler = Scaler(screen_info)
        surface = pygame.Surface(scaler.scale(self._options['dimensions']))
        surface.fill((255, 255, 255))

        font = pygame.font.Font(None, self._options['font_size'])

        y_pos = 0

        height = scaler.scale(self._options['dimensions'])[1]
        self._list.set_page_size(int(float(height) / self._options['font_size']))

        # Get the list and draw it
        list_index = 0
        for item in self._list.get_current_page():
            if list_index == self._position:
                text = font.render(item[1], True, (255, 0, 0))
            else:
                text = font.render(item[1], True, self._options['foreground_color'])
            text_rect = text.get_rect()
            text_rect.centerx = surface.get_rect().centerx
            text_rect.top = y_pos
            y_pos += self._options['font_size']
            surface.blit(text, text_rect)
            list_index += 1

        # Draw the pages underneath

        canvas.blit(surface, scaler.scale(self._options['position']))

    def set_list(self, list):
        self._list = list

    def next_page(self):
        self._list.next_page()

    def previous_page(self):
        self._list.previous_page()

    def set_page(self, page):
        self._list.set_page(page)

    def set_position(self, position):
        self._position = position

    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self._position > 0:
                    self._position -= 1
                return True, '', {}
            elif event.key == pygame.K_DOWN:
                if self._position < self._list.get_page_size() - 1:
                    self._position += 1
                return True, '', {}
            elif event.key == pygame.K_LEFT:
                self.previous_page()
                return True, '', {}
            elif event.key == pygame.K_RIGHT:
                self.next_page()
                return True, '', {}

        return False, '', {}
