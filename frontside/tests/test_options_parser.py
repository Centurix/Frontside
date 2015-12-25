# -*- coding: utf-8 -*-
from frontside import OptionsParser
import mock


def test_options():
    parser_mock = mock.Mock()
    parser_mock.parse_args = mock.Mock(return_value=(1, 1))
    with mock.patch('optparse.OptionParser', return_value=parser_mock, ):
        options = OptionsParser.parse('description', 'version')
        assert parser_mock.parse_args.call_count == 1
        assert options == 1
