# -*- coding: utf-8 -*-
import threading
import sqlite3
from mame import Mame
from repositories import RomRepository
from observable import Observable


class Scanner(threading.Thread, Observable):
    def __init__(self, config):
        self.__config = config
        self.__mame = None
        self.__connection = None
        Observable.__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        self.__mame = Mame(self.__config)
        self.__connection = sqlite3.connect(self.__config['frontside']['database_path'])
        rom_list = self.__mame.list_full()
        rom_repository = RomRepository(self.__connection)
        rom_repository.add_rom_name_and_description_from_array(rom_list)
        # print('Starting the thread')
        # for i in range(0, 1000000):
        #     self.notify_observers(i)
