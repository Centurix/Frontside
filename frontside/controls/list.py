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
            'lines': 10
        }
        self._list = ListProvider(None)
        self._position = 0
        super(self.__class__, self).__init__(default, options)

    def draw(self, canvas, screen_info):
        scaler = Scaler(screen_info)
        surface = pygame.Surface(scaler.scale(self._options['dimensions']))
        surface.fill((255, 255, 255))

        self._list.set_page_size(self._options['lines'])

        height = scaler.scale(self._options['dimensions'])[1]
        font_size = int(float(height) / self._options['lines'])
        font = pygame.font.Font(None, font_size)

        # Get the list and draw it
        list_index = 0
        current_page = self._list.get_current_page()

        # Make sure the current cursor is within bounds
        if self._position > len(current_page) - 1:
            self._position = len(current_page) - 1

        for item in current_page:
            if list_index == self._position:
                text = font.render(item[1], True, (255, 0, 0))
            else:
                text = font.render(item[1], True, self._options['foreground_color'])
            text_rect = text.get_rect()
            text_rect.centerx = surface.get_rect().centerx
            text_rect.top = list_index * font_size
            surface.blit(text, text_rect)
            list_index += 1

        # Draw the pages underneath

        canvas.blit(surface, scaler.scale(self._options['position']))

    def set_list(self, list_provider):
        self._list = list_provider

    def get_list(self):
        return self._list

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
            elif event.key == pygame.K_LEFT or event.key == pygame.K_PAGEUP:
                self.previous_page()
                return True, '', {}
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_PAGEDOWN:
                self.next_page()
                return True, '', {}

        return False, '', {}

    def get_selection(self):
        return self._list.get_current_page()[self._position][0]
