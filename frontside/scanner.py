# -*- coding: utf-8 -*-
import threading
import sqlite3
from mame import Mame
from repositories import RomRepository
from observable import Observable


class Scanner(Observable, threading.Thread):
    def __init__(self, config):
        self._config = config
        self._mame = None
        self._connection = None
        self._running = False
        Observable.__init__(self)
        threading.Thread.__init__(self)

    def halt(self):
        self._mame.halt()

    def get_status(self):
        return self._mame.get_status()

    def run(self):
        self._running = True
        """
        1. Get a list of actual ROM files in the rom_path
        2. Filter against the ROM names from MAME
        3. Depending on the amount, select the most optimal metadata retrieval method
            a. Gather full metadata from MAME for each ROM
            b. Gather full metadata for ALL MAME ROMs

        Some systems only have a handful of ROMs in the directory, so a) is much quicker, whereas some
        systems have ALL 32k ROMs, so b) would be quicker.
        :return:
        """
        print 'Starting the thread'
        self._mame = Mame(self._config)
        self._connection = sqlite3.connect(self._config['frontside']['database_path'])

        # self._mame.register_observer(self)
        # found_roms = self._mame.list_rom_files()

        self._mame.register_observer(self)
        self._mame.list_xml()

        # roms = mame.list_full()
        # roms = mame.list_xml()
        # repository = RomRepository(self._connection)
        # repository.register_observer(self)
        # repository.add_rom_name_and_description_from_array(roms)
        # repository.add_rom_details_from_array(roms)

        # for rom in mame_roms:
        #     print rom

        # rom_list = self.__mame.list_full()
        # rom_repository = RomRepository(self.__connection)
        # rom_repository.add_rom_name_and_description_from_array(rom_list)

        # self.__mame.register_observer(self)
        # roms = self.__mame.list_xml()
        # repository = RomRepository(self.__connection)
        # repository.add_rom_details_from_array(roms)
        self._running = False

    def notify(self, observable, current_line, line_count):
        self.notify_observers(current_line, line_count)
