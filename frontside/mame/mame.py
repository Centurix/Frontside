# -*- coding: utf-8 -*-
import subprocess
import re


class Mame(object):
    def __init__(self, config):
        """
        Do all M.A.M.E. related stuff in here, each one returns stdout
        :param config: config object with the M.A.M.E. exec path and ROM path
        :return:
        """
        self.mame = config['frontside']['mame_exec']
        self.rom_path = config['frontside']['rom_path']

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
                "description": line[18:].replace('"', '').rstrip()
            })
        roms.pop(0)
        return roms

    def list_xml(self, rom_name=None):
        params = [self.mame, '-rompath', self.rom_path, '-listxml']
        if rom_name is None:
            params.append(rom_name)
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout

    def play(self, rom_name):
        process = subprocess.Popen([self.mame, '-rompath', self.rom_path, rom_name], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout

    def version(self):
        process = subprocess.Popen([self.mame, '-?'], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        results = re.search('v0.(\d{3}) ', stdout.splitlines()[0])

        return int(results.group(1))
