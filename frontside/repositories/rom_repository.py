# -*- coding: utf-8 -*-
from ..models import Roms
from ..models import Metadata
import sys
from time import sleep
from repository import Repository


class RomRepository(Repository):
    def __init__(self, connection):
        super(self.__class__, self).__init__(connection)
        self._connection = connection

    def add_rom_name_and_description_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection using an array of ROM dictionaries
        :param self:
        :param rom_collection:
        :return:
        """
        Roms(self._connection).truncate()
        for rom in rom_collection:
            Roms(self._connection).insert(rom).save(commit=False)

        self._connection.commit()

    def add_rom_details_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection
        :param rom_collection:
        :return:
        """
        metadata = Metadata(self._connection)
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

        self._connection.commit()
        metadata.fast_off()

    def list_roms(self):
        """
        Provide a list of ROMs via a filter
        :param filter:
        :return:
        """
        return Roms(self._connection).select(['rom', 'description']).get_all()

    def get_rom_page(self, page, page_size):
        """
        Return a page from the ROM table
        :param page:
        :param page_size:
        :return:
        """
        return Roms(self._connection).select(['rom', 'description']).page_size(page_size).page_offset(page).get_all()

    def get_rom_page_count(self, page, page_size):
        """
        Return the total page count of ROMs
        :param page:
        :param page_size:
        :return:
        """
        total_roms = Roms(self._connection).page_size(page_size).page_offset(page).get_count()
        return int(float(total_roms) / page_size)
