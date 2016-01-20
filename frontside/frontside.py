# -*- coding: utf-8 -*-
import sqlite3
from database import DatabaseMigration
from mame import Mame
from scanner import Scanner
import sys
from time import sleep
from repositories import RomRepository

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
        mame.register_observer(self)
        roms = mame.list_xml()  # 1:04
        repository = RomRepository(connection)
        repository.add_rom_details_from_array(roms)
        print len(roms)
        # print("\n%d" % len(roms))
        # mame.play('pengo')
        # scanner = Scanner(self.__config)
        # scanner.register_observer(self)
        # scanner.start()

    def notify(self, observable, current_line, line_count):
        percent = float(current_line) / line_count * 100
        done = ('#' * int(float(50) / 100 * percent)) + ('-' * 50)
        sys.stdout.write('\r|%s| (%.2f%%)' % (done[:50], float(current_line) / line_count * 100))
        sys.stdout.flush()

        sleep(.001)
