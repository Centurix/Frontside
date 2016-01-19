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
                "description": line[18:].replace('"', '')
            })
        roms.pop(0)
        return roms

    def list_xml(self, rom_name=None):
        params = [self.mame, '-rompath', self.rom_path, '-listxml']
        if rom_name is not None:
            params.append(rom_name)
        process = subprocess.Popen(params, stdout=subprocess.PIPE)
        roms = []
        rom = None

        machine = re.compile('name="(?P<name>.*?)".*cloneof="(?P<cloneof>.*?).*romof="(?P<romof>.*?)"')
        description = re.compile('(?P<description>.*?)</description>')
        year = re.compile('(?P<year>.*?)</year>')
        manufacturer = re.compile('(?P<manufacturer>.*?)</manufacturer>')
        driver = re.compile('status="(?P<status>.*?)".*emulation="(?P<emulation>.*?)".*color="(?P<color>.*?)".*sound="(?P<sound>.*?)".*graphic="(?P<graphic>.*?)".*savestate="(?P<savestate>.*?)"')

        for line in iter(process.stdout.readline, ''):
            # Check for important stuff
            if line[1:9] == "<machine":
                m = machine.match(line[10:])
                if m is not None:
                    rom = {
                        "rom": m.group('name'),
                        "cloneof": m.group('cloneof'),
                        "romof": m.group('romof')
                    }
            elif line[2:15] == "<description>":
                m = description.match(line[15:])
                if m is not None and rom is not None:
                        rom['description'] = m.group('description')
            elif line[2:8] == "<year>":
                m = year.match(line[8:])
                if m is not None and rom is not None:
                        rom['year'] = m.group('year')
            elif line[2:16] == "<manufacturer>":
                m = manufacturer.match(line[16:])
                if m is not None and rom is not None:
                        rom['manufacturer'] = m.group('manufacturer')
            elif line[2:9] == "<driver":
                m = driver.match(line[10:])
                if m is not None and rom is not None:
                        rom['status'] = m.group('status')
                        rom['emulation'] = m.group('emulation')
                        rom['color'] = m.group('color')
                        rom['sound'] = m.group('sound')
                        rom['graphic'] = m.group('graphic')
                        rom['savestate'] = m.group('savestate')
            elif line[1:11] == "</machine>":
                # Do we have a full quota of data? Yes, save it, no, proceed!
                if rom is not None:
                    roms.append(rom)
                rom = None
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
