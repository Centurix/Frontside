# -*- coding: utf-8 -*-
import subprocess
import re
from ..observable import Observable


class Mame(Observable):
    def __init__(self, config):
        """
        Do all M.A.M.E. related stuff in here, each one returns stdout
        :param config: config object with the M.A.M.E. exec path and ROM path
        :return:
        """
        self.mame = config['frontside']['mame_exec']
        self.rom_path = config['frontside']['rom_path']
        Observable.__init__(self)

    def list_full(self, rom_name=None):
        params = [self.mame, '-rompath', self.rom_path, '-listfull']
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
        params = [self.mame, '-rompath', self.rom_path, '-listxml']
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
        process = subprocess.Popen([self.mame, '-rompath', self.rom_path, rom_name], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout

    def version(self):
        process = subprocess.Popen([self.mame, '-?'], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        results = re.search('v0.(\d{3}) ', stdout.splitlines()[0])

        return int(results.group(1))

    def rom_count(self):
        params = [self.mame, '-rompath', self.rom_path, '-listfull']
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return len(stdout.split('\n')) - 1
