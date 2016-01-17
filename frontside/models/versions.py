# -*- coding: utf-8 -*-
from model import Model


class Versions(Model):
    def __init__(self, connection):
        super(self.__class__, self).__init__(connection)
        self.table = "versions"
