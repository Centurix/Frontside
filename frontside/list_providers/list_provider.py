# -*- coding: utf-8 -*-


class ListProvider(object):
    def __init__(self, connection):
        self._page = 0
        self._page_size = 10
        self._connection = connection
        self._repository = None
        self._dirty = True
        self._cache = None
        self._page_count = 1

    def next_page(self):
        if self._page < self._page_count:
            self._page += 1
            self._dirty = True

    def previous_page(self):
        if self._page > 0:
            self._page -= 1
            self._dirty = True

    def set_page(self, page):
        if self._page != page:
            self._page = page
            self._dirty = True

    def set_page_size(self, page_size):
        if self._page_size != page_size:
            self._page_size = page_size
            self._dirty = True

    def get_page_size(self):
        return self._page_size

    def get_current_page(self):
        if self._dirty:
            self._cache = ['Empty list']

        return self._cache
