# -*- coding: utf-8 -*-
from ..controls import Button
from ..controls import Container
from ..controls import List
from ..controls import Text


class Control(object):
    @staticmethod
    def factory(control_type, options):
        if control_type == 'button':
            return Button(options)
        if control_type == 'container':
            return Container(options)
        if control_type == 'list':
            return List(options)
        if control_type == 'text':
            return Text(options)

        return Button(options)
