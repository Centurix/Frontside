# -*- coding: utf-8 -*-
from abc import ABCMeta


class Observable(object):
    """
    Abstract class for observers
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)
