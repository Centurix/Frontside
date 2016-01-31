# -*- coding: utf-8 -*-
from controls import Button


class Theme(object):
    """
    Theme related stuff
    """
    def __init__(self, theme):
        self._theme = theme

    def __getitem__(self, screen):
        gg = {}
        execfile('themes/%s/%s.py' % (self._theme, screen), gg)
        return Screen(gg[screen])


class Screen(object):
    """
    Single screen instance
    """
    def __init__(self, screen_def):
        """
        Create a concrete representation of the screens layout
        :param screen_def:
        :return:
        """
        self._screen_def = screen_def
        self.controls = []
        focus = True
        for control in self._screen_def['controls']:
            if control['type'] == 'button':
                self.controls.append(Button(
                    dimensions=(control['width'], control['height']),
                    background_color=(128, 128, 128),
                    foreground_color=(0, 0, 0),
                    text=control['text'],
                    focused=focus,
                    position=(control['left'], control['top'])
                ))
                focus = False

    def render(self, canvas):
        for control in self.controls:
            control.draw(canvas)

    def process_event(self, event):
        """
        Process an event for the control with the focus
        :param event:
        :return:
        """
        for control in self.controls:
            if control.process_event(event):
                break
