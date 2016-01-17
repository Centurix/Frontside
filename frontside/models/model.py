# -*- coding: utf-8 -*-
from abc import ABCMeta


class Model(object):
    """
    Abstract class for a basic model, make sure __init__ is called
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        self.table = ""
        self.predicate_fields = []
        self.select_fields = []
        self.order_fields = []
        self.insert_fields = {}
        self.update_fields = {}
        self._page_size = 0
        self._page_offset = 0
        self._connection = connection
        self.cursor = self._connection.cursor()

    def truncate(self):
        """
        Remove all ROMs from the database
        :return:
        """
        self.cursor.execute("DELETE FROM %s" % self.table)
        self.cursor.execute("VACUUM")
        self._connection.commit()
        return self

    def where(self, predicate_fields):
        """
        Add the predicates to the model
        :param predicate_fields:
        :return:
        """
        if type(predicate_fields) == str:
            self.predicate_fields.append(predicate_fields)
        else:
            self.predicate_fields += predicate_fields

        return self

    def select(self, select_fields):
        """
        Add the fields to select to the model
        :param select_fields:
        :return:
        """
        if type(select_fields) == str:
            self.select_fields.append(select_fields)
        else:
            self.select_fields += select_fields

        return self

    def order_by(self, order_fields):
        """
        Set the ordering
        :param order_fields:
        :return:
        """
        if type(order_fields) == str:
            self.order_fields.append(order_fields)
        else:
            self.order_fields += order_fields

        return self

    def page_size(self, page_size):
        """
        Set the page size
        :param page_size:
        :return:
        """
        self._page_size = page_size

        return self

    def page_offset(self, page_offset):
        """
        Set the page offset
        :param page_offset:
        :return:
        """
        self._page_offset = page_offset

        return self

    def get_all(self):
        """
        Retrieve all rows for the query
        :return:
        """
        return self.cursor.execute(self.build_select_query()).fetchall()

    def get(self):
        """
        Retrieve the first row only
        """
        return self.cursor.execute(self.build_select_query()).fetchone()

    def get_selects(self):
        if len(self.select_fields) == 0:
            return "*"

        return ",".join(self.select_fields)

    def get_predicates(self):
        if len(self.predicate_fields) == 0:
            return ""

        return "WHERE %s" % (" AND ".join(self.predicate_fields))

    def get_order_by(self):
        if len(self.order_fields) == 0:
            return ""

        return "ORDER BY %s" % (",".join(self.order_fields))

    def get_paging(self):
        if self._page_size == 0:
            return ""

        return "LIMIT %d, %d" % (self._page_offset * self._page_size, self._page_size)

    def insert(self, insert_fields):
        if not type(insert_fields) == dict:
            raise

        self.update_fields = dict()
        self.insert_fields = dict(self.insert_fields.items() + insert_fields.items())

        return self

    def update(self, update_fields):
        if not type(update_fields) == dict:
            raise

        self.insert_fields = dict()
        self.update_fields = dict(self.update_fields.items() + update_fields.items())

        return self

    def save(self, commit=True):
        if len(self.insert_fields) > 0:
            self.cursor.execute(self.build_insert_query())
            if commit:
                self._connection.commit()
        else:
            self.cursor.execute(self.build_update_query())
            if commit:
                self._connection.commit()

        return self

    def delete(self, commit=True):
        self.cursor.execute(self.build_delete_query())
        if commit:
            self._connection.commit()

        return self

    def build_select_query(self):
        return "SELECT %s FROM %s %s %s %s" % (
            self.get_selects(),
            self.table,
            self.get_predicates(),
            self.get_order_by(),
            self.get_paging()
        )

    def build_insert_query(self):
        fields = "`" + ("`,`".join([key for key, value in self.insert_fields.items()])) + "`"
        values = "'" + ("','".join([str(value) for key, value in self.insert_fields.items()])) + "'"

        return "INSERT INTO %s (%s) VALUES (%s)" % (self.table, fields, values)

    def build_update_query(self):
        fields = ",".join(["`" + key + "`='" + value + "'" for key, value in self.update_fields.items()])

        return "UPDATE %s SET %s %s" % (self.table, fields, self.get_predicates())

    def build_delete_query(self):
        return "DELETE FROM %s %s" % (self.table, self.get_predicates())