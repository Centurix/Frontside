# -*- coding: utf-8 -*-
from ..models import Profiles
from repository import Repository


class ProfileRepository(Repository):
    def __init__(self, connection):
        super(self.__class__, self).__init__(connection)
        self.__connection = connection

    def get_all_profiles(self):
        profiles = Profiles(self.__connection)
        return profiles.select(['name', 'avatar']).order_by('name').get_all()

    def seed_profiles(self):
        profiles = Profiles(self.__connection)
        profiles.truncate()
        profiles.insert({
            'name': 'Chris Read',
            'avatar': 'chris.png'
        }).save()
        profiles.insert({
            'name': 'John Smith',
            'avatar': 'john.png'
        }).save()
