# -*- coding: utf-8 -*-
import abc


class Repository(object):
    """
    Abstract class for a basic repository, make sure __init__ is called
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, connection):
        pass