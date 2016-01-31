# -*- coding: utf-8 -*-
from abc import ABCMeta


class Control(object):
    """
    Abstract class for a basic model, make sure __init__ is called
    """
    __metaclass__ = ABCMeta

    def __init__(self, focused):
        self.focused = focused
