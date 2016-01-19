# -*- coding: utf-8 -*-
import sqlite3
from database import DatabaseMigration
from mame import Mame
from scanner import Scanner

"""
How do we manage the ROM list generation?
"""


class Frontside(object):
    """
    The main Frontside application
    """
    def __init__(self, config):
        self.__config = config

    def start(self):
        # Connect and migrate where necessary
        connection = sqlite3.connect(self.__config['frontside']['database_path'])
        DatabaseMigration(connection)

        mame = Mame(self.__config)
        roms = mame.list_xml('pengo')
        print(roms)
        # mame.play('pengo')
        # scanner = Scanner(self.__config)
        # scanner.register_observer(self)
        # scanner.start()

    def notify(self, observable, percentage):
        print('Progress updated: %d%%' % percentage)
