# -*- coding: utf-8 -*-
import subprocess
import re
import os

from ..observable import Observable


class Mame(Observable):
    def __init__(self, config):
        """
        Do all M.A.M.E. related stuff in here, each one returns stdout
        :param config: config object with the M.A.M.E. exec path and ROM path
        :return:
        """
        self.__mame = config['frontside']['mame_exec']
        self.__rom_path = config['frontside']['rom_path']
        Observable.__init__(self)

    def list_rom_names(self):
        """
        ROM names only, complete list
        :return:
        """
        params = [self.__mame, '-rompath', self.__rom_path, '-listfull']
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        roms = []
        for line in stdout.split('\n'):
            roms.append(line[:17].rstrip())
        roms.pop(0)
        return roms

    def list_full(self, rom_name=None):
        """
        ROM names and description as a dictionary
        :param rom_name:
        :return:
        """
        params = [self.__mame, '-rompath', self.__rom_path, '-listfull']
        if rom_name is not None:
            params.append(rom_name)
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        roms = []
        for line in stdout.split('\n'):
            roms.append({
                "rom": line[:17].rstrip(),
                "description": line[18:].replace('"', '')
            })
        roms.pop(0)
        return roms

    def list_xml(self, rom_name=None):
        """
        Detailed ROM metadata in dictionary format
        :param rom_name:
        :return:
        """
        params = [self.__mame, '-rompath', self.__rom_path, '-listxml']
        total_roms = self.rom_count()
        if rom_name is not None:
            params.append(rom_name)
            total_roms = 1
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        roms = []
        rom = None
        rom_count = 0
        for line in iter(process.stdout.readline, ''):
            if line.strip('\t')[:4] not in ['<mac', '<des', '<yea', '<man', '<dri']:
                continue
            if line[1:9] == "<machine":
                if rom is not None and 'year' in rom:
                    rom_count += 1
                    self.notify_observers(rom_count, total_roms)
                    roms.append(rom)
                rom = {k: v for k, v in (part.replace('"', '').split('=') for part in line[10:].strip('<>"\/\n').split(' '))}
            elif line[2:15] == "<description>":
                rom['description'] = line[15:-15]
            elif line[2:8] == "<year>":
                rom['year'] = line[8:-8]
            elif line[2:16] == "<manufacturer>":
                rom['manufacturer'] = line[16:-16]
            elif line[2:9] == "<driver":
                rom = dict(rom.items() + {k: v for k, v in (part.replace('"', '').split('=') for part in line[10:].strip('<>"\/\n').split(' '))}.items())

        self.notify_observers(1, 1)
        return roms

    def play(self, rom_name):
        """
        Play a ROM
        :param rom_name:
        :return:
        """
        process = subprocess.Popen([self.__mame, '-rompath', self.__rom_path, rom_name], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout

    def version(self):
        """
        Retrieve MAME version
        :return:
        """
        process = subprocess.Popen([self.__mame, '-?'], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        results = re.search('v0.(\d{3}) ', stdout.splitlines()[0])

        return int(results.group(1))

    def rom_count(self):
        """
        Return the total ROM count
        :return:
        """
        params = [self.__mame, '-rompath', self.__rom_path, '-listfull']
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return len(stdout.split('\n')) - 1

    def list_rom_files(self):
        """
        Return a list of the ROM files in the MAME rom directory
        :return:
        """
        rom_files = os.listdir(self.__rom_path)
        valid_roms = []
        rom_count = 0
        for rom_file in rom_files:
            if rom_file.endswith('.7z'):
                valid_roms.append(rom_file[:-3])
            elif rom_file.endswith('.zip'):
                valid_roms.append(rom_file[:-4])
            self.notify_observers(rom_count, len(rom_files))
            rom_count += 1

        self.notify_observers(1, 1)

        return set.intersection(set(valid_roms), set(self.list_rom_names()))
