from pathlib import Path

from litelookup.config import config


def test_is_valid_APIkey():
    assert config.is_valid_APIkey("gsk_123456") is True
    assert config.is_valid_APIkey("abc_123456") is False
    assert config.is_valid_APIkey("") is False


def test_get_config_dir():
    expected_path = Path.home() / ".config/litelookup"
    assert config.get_config_dir() == expected_path


def test_get_config_file():
    expected_path = Path.home() / ".config/litelookup/config.ini"
    assert config.get_config_file() == expected_path
