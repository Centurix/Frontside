# -*- coding: utf-8 -*-
from ..models import Roms
from ..models import Metadata
import sys
from time import sleep


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

    def add_rom_details_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection
        :param rom_collection:
        :return:
        """
        metadata = Metadata(self.__connection)
        metadata.truncate()
        metadata.fast_on()
        counter = 0
        for rom in rom_collection:
            # percent = float(counter) / len(rom_collection) * 100
            # done = ('#' * int(float(50) / 100 * percent)) + ('-' * 50)
            # sys.stdout.write('\r|%s| (%.2f%%)' % (done[:50], percent))
            # sys.stdout.flush()
            #
            # sleep(.000001)
            #
            # counter += 1
            metadata.insert(rom).save(commit=False)

        self.__connection.commit()
        metadata.fast_off()
