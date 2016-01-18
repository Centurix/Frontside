# -*- coding: utf-8 -*-
from ..models import Roms


class RomRepository(object):
    def __init__(self, connection):
        self.__connection = connection

    def add_rom_name_and_description_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection using an array of ROM dictionaries
        :param self:
        :param rom_collection:
        :return:
        """
        Roms(self.__connection).truncate()
        for rom in rom_collection:
            Roms(self.__connection).insert(rom).save(commit=False)

        self.__connection.commit()
