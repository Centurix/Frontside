# -*- coding: utf-8 -*-
from ..models import Roms
from ..models import Metadata
from repository import Repository
from ..observable import Observable


class RomRepository(Observable, Repository):
    def __init__(self, connection):
        Repository.__init__(self, connection)
        # super(self.__class__, self).__init__(connection)
        self._connection = connection
        Observable.__init__(self)

    def add_rom_name_and_description_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection using an array of ROM dictionaries
        :param self:
        :param rom_collection:
        :return:
        """
        roms = Roms(self._connection)
        roms.truncate()
        roms.fast_on()
        rom_count = 0
        for rom in rom_collection:
            roms.insert(rom).save(commit=False)
            self.notify_observers(rom_count, len(rom_collection))
            rom_count += 1

        self.notify_observers(1, 1)

        self._connection.commit()
        roms.fast_off()

    def add_rom_details_from_array(self, rom_collection):
        """
        Add the ROMs from the rom_collection
        :param rom_collection:
        :return:
        """
        metadata = Metadata(self._connection)
        metadata.truncate()
        metadata.fast_on()
        rom_count = 0
        for rom in rom_collection:
            metadata.insert(rom).save(commit=False)
            self.notify_observers(rom_count, len(rom_collection))
            rom_count += 1

        self.notify_observers(1, 1)

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

    def get_favourites_page(self, page, page_size):
        """
        Return a page from the ROM table
        :param page:
        :param page_size:
        :return:
        """
        roms = Roms(self._connection)
        roms._debug = True
        return roms.select(['rom', 'description']).page_size(page_size).page_offset(page).order_by('rom desc').get_all()

    def get_favourites_page_count(self, page, page_size):
        """
        Return the total page count of ROMs
        :param page:
        :param page_size:
        :return:
        """
        total_roms = Roms(self._connection).page_size(page_size).page_offset(page).get_count()
        return int(float(total_roms) / page_size)
