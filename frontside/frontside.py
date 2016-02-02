# -*- coding: utf-8 -*-
import sqlite3
from database import DatabaseMigration
# import pygame
# from theme import Theme
from screens import AllGames

# from mame import Mame
# from scanner import Scanner
# import sys
# import time
# from repositories import RomRepository
from repositories import ProfileRepository

"""
How do we manage the ROM list generation?
"""


class Frontside(object):
    """
    The main Frontside application
    """
    def __init__(self, config):
        self._config = config

    def start(self):
        """
        At this point the application has bootstrapped and provided a merged config from the command line
        and the configuration file. We are effectively processing whatever we want.
        :return:
        """

        # Connect and migrate where necessary, would be nice for a database object that has a connection
        # and the ability to migrate the database automatically where needed.
        connection = sqlite3.connect(self._config['frontside']['database_path'])
        DatabaseMigration(connection)

        """
        At this point we need to read the definition of the screen for the UI elements from a file somewhere

        Screen management
        =================

        We want several types of screens

        1. Full screen layout with event processing, several exit points
        2. Full screen layout with event processing, a single exit point returning packaged data
        3. Smaller overlay screen with event processing, like a modal, a single exit point returning packaged data

        Each thing covers the events and display

        +-------+  +--------------+  +-------------------------+  +-------------+
        | Entry |->| Blank Screen |->| Profile selection modal |->| Main screen |
        +-------+  +--------------+  +-------------------------+  +-------------+

        Invoke display plus process events

        main_screen.show(canvas)

        Within the main_screen, show the transparent overlay selection

        if button_clicked:
            profile_selection.show(canvas)

        Are there any profiles? Have we selected a profile in the config?
        """
        profiles = ProfileRepository(connection)
        profiles.seed_profiles()

        AllGames(self._config).show()

        # if len(profiles.get_all_profiles()) > 0 and self._config['frontside']['profile'] == '':
        #     """
        #     Show the profile selector
        #
        #     Ideally we'd like to get values from a screen in a prompt style situation. We either return values or we cancel.
        #
        #     """
        #     profile = thing.prompt(layout)
        #
        #     profile_selection = theme['profile_selection']
        #     profile_selection.render(screen)
        #     pygame.display.flip()
        #     while not complete:
        #         clock.tick(60)
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:
        #                 complete = True
        #             elif event.type == pygame.KEYDOWN:
        #                 if (event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL) or \
        #                    (event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT):
        #                     complete = True
        #             profile_selection.process_event(event)
        #
        #         profile_selection.render(screen)
        #         pygame.display.flip()
        #
        # main = theme['main']
        #
        # while not complete:
        #     clock.tick(60)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             complete = True
        #         elif event.type == pygame.KEYDOWN:
        #             if (event.key == pygame.K_w and event.mod & pygame.KMOD_CTRL) or \
        #                (event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT):
        #                 complete = True
        #         main.process_event(event)
        #
        #     main.render(screen)
        #     pygame.display.flip()

        # mame = Mame(self._config)
        # mame.register_observer(self)
        # roms = mame.list_xml()
        # repository = RomRepository(connection)
        # repository.add_rom_details_from_array(roms)
        # mame.play('pengo')
        # scanner = Scanner(self._config)
        # scanner.register_observer(self)
        # scanner.start()

    # def notify(self, observable, current_line, line_count):
    #     percent = float(current_line) / line_count * 100
    #     done = ('#' * int(float(50) / 100 * percent)) + ('-' * 50)
    #     sys.stdout.write('\r|%s| (%.2f%%)' % (done[:50], percent))
    #     sys.stdout.flush()
    #
    #     time.sleep(.000001)
