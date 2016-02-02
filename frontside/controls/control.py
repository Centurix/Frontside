# -*- coding: utf-8 -*-
import abc


class Control(object):
    """
    Abstract class for a basic model, make sure __init__ is called
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, focused):
        self.focused = focused

    @abc.abstractmethod
    def draw(self, canvas):
        pass

    @abc.abstractmethod
    def process_event(self, event):
        if not self.focused:
            return False, '', {}

        return False, '', {}
