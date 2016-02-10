# -*- coding: utf-8 -*-
from list_provider import ListProvider
from ..repositories import RomRepository


class FavouritesProvider(ListProvider):
    def __init__(self, connection):
        super(self.__class__, self).__init__(connection)
        self._repository = RomRepository(self._connection)

    def get_current_page(self):
        if self._dirty:
            self._cache = self._repository.get_favourites_page(self._page, self._page_size)
            self._page_count = self._repository.get_favourites_page_count(self._page, self._page_size)
            self._dirty = False

        return self._cache
