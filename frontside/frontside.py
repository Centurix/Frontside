# -*- coding: utf-8 -*-
import sqlite3
from database import DatabaseMigration
import pygame
from controls import Button
from theme import Theme

from mame import Mame
from scanner import Scanner
import sys
import time
from repositories import RomRepository
from repositories import ProfileRepository

"""
How do we manage the ROM list generation?
"""


class Frontside(object):
    """
    The main Frontside application
    """
    def __init__(self, config):
        self.__config = config

    def start(self):
        """
        At this point the application has bootstrapped and provided a merged config from the command line
        and the configuration file. We are effectively processing whatever we want.
        :return:
        """

        # Connect and migrate where necessary, would be nice for a database object that has a connection
        # and the ability to migrate the database automatically where needed.
        connection = sqlite3.connect(self.__config['frontside']['database_path'])
        DatabaseMigration(connection)

        # Open a window
        pygame.init()
        width = self.__config['frontside']['width']
        height = self.__config['frontside']['height']
        screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

        """
        At this point we need to read the definition of the screen for the UI elements from a file somewhere
        """

        clock = pygame.time.Clock()
        complete = False

        theme = Theme(self.__config['frontside']['theme'])

        """
        Are there any profiles? Have we selected a profile in the config?
        """
        profiles = ProfileRepository(connection)
        profiles.seed_profiles()
        if len(profiles.get_all_profiles()) > 0 and self.__config['frontside']['profile'] == '':
            """
            Show the profile selector
            """
            profile_selection = theme['profile_selection']
            profile_selection.render(screen)
            pygame.display.flip()
            while not complete:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        complete = True
                    elif event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL) or \
                           (event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT):
                            complete = True
                    profile_selection.process_event(event)

                profile_selection.render(screen)
                pygame.display.flip()

        main = theme['main']

        while not complete:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    complete = True
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL) or \
                       (event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT):
                        complete = True
                main.process_event(event)

            main.render(screen)
            pygame.display.flip()

        # mame = Mame(self.__config)
        # mame.register_observer(self)
        # roms = mame.list_xml()
        # repository = RomRepository(connection)
        # repository.add_rom_details_from_array(roms)
        # mame.play('pengo')
        # scanner = Scanner(self.__config)
        # scanner.register_observer(self)
        # scanner.start()

    # def notify(self, observable, current_line, line_count):
    #     percent = float(current_line) / line_count * 100
    #     done = ('#' * int(float(50) / 100 * percent)) + ('-' * 50)
    #     sys.stdout.write('\r|%s| (%.2f%%)' % (done[:50], percent))
    #     sys.stdout.flush()
    #
    #     time.sleep(.000001)
