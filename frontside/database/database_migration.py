# -*- coding: utf-8 -*-
import sqlite3


class DatabaseMigration(object):
    """
    Check the database and migrate if necessary
    """
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.migrate()

    def migrate(self):
        migrations = self.get_migration_methods()
        version = self.get_version()
        for change_version in sorted(migrations):
            if change_version > version:
                migrations[change_version]()
                self.update_version(change_version)

    def downgrade(self, version):
        downgrades = self.get_downgrade_methods()
        for change_version in sorted(downgrades, reverse=True):
            if change_version >= version:
                downgrades[change_version]()
                self.update_version(change_version)

    def get_version(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS versions (version INT NULL, type CHAR(1) NOT NULL)")
            self.cursor.execute("SELECT version FROM versions WHERE type='d'")
            version = self.cursor.fetchone()
            if version is not None:
                return version[0]

        except sqlite3.Error:
            pass

        return 0

    def get_migration_methods(self):
        migrations = {}
        for method in dir(self):
            attr = getattr(self, method)
            if callable(attr) and method[:9] == "migration":
                migrations[int(attr.__doc__)] = attr

        return migrations

    def get_downgrade_methods(self):
        downgrades = {}
        for method in dir(self):
            attr = getattr(self, method)
            if callable(attr) and method[:9] == "downgrade":
                downgrades[int(attr.__doc__)] = attr

        return downgrades

    def update_version(self, version):
        """
        Update database version
        :param version:
        :return:
        """
        self.cursor.execute("DELETE FROM versions WHERE type='d'")
        self.cursor.execute("INSERT INTO versions (version, type) VALUES ('%s', 'd')" % version)
        self.connection.commit()

    def migration_create_roms(self):
        """1"""
        self.cursor.execute(
            "CREATE TABLE roms "
            "(rom VARCHAR(14) NOT NULL, "
            "description VARCHAR(150) NULL, "
            "found INT NOT NULL DEFAULT(0))"
        )
        self.cursor.execute("CREATE INDEX idx_roms on roms (rom ASC, description ASC, found ASC)")

    def downgrade_create_roms(self):
        """1"""
        self.cursor.execute("DROP TABLE roms")

    def migration_create_metadata(self):
        """2"""
        self.cursor.execute(
            "CREATE TABLE metadata ("
            "name VARCHAR(14) NOT NULL, "
            "year VARCHAR(20) NULL, "
            "manufacturer VARCHAR(64) NULL, "
            "players INT NULL, "
            "status VARCHAR(10) NULL, "
            "emulation VARCHAR(10) NULL, "
            "color VARCHAR(10) NULL, "
            "sound VARCHAR(10) NULL,"
            "graphic VARCHAR(10) NULL,"
            "cloneof VARCHAR(14) NULL,"
            "savestate VARCHAR(20) NULL"
            ")"
        )

    def downgrade_create_metadata(self):
        """2"""
        self.cursor.execute("DROP TABLE metadata")
