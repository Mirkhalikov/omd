from unittest.mock import patch
import sys
import os
sys.path.append(os.getcwd())
from what_is_year_now import what_is_year_now


@patch('urllib.request.urlopen')
@patch('json.load')
def test_what_is_year_now_ymd_format(mock_load, mock_urlopen):
    mock_load.return_value = {'currentDateTime': '2023-11-03'}
    result = what_is_year_now()
    assert result == 2023


@patch('urllib.request.urlopen')
@patch('json.load')
def test_what_is_year_now_dmy_format(mock_load, mock_urlopen):
    mock_load.return_value = {'currentDateTime': '01.03.2019'}
    result = what_is_year_now()
    assert result == 2019


@patch('urllib.request.urlopen')
@patch('json.load')
def test_what_is_year_now_invalid_format(mock_load, mock_urlopen):
    mock_load.return_value = {'currentDateTime': '2023/11/03'}
    try:
        result = what_is_year_now()
    except ValueError as e:
        assert str(e) == 'Invalid format'
    else:
        assert False, 'Expected TypeError to be raised'
