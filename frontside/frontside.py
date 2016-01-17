# -*- coding: utf-8 -*-
from mame import Mame

"""
How do we manage the ROM list generation?

"""


class Frontside(object):
    """
    The main Frontside application
    """
    def __init__(self, config):
        self.config = config

    def start(self):
        mame = Mame(self.config)
        mame.play('pengo')
