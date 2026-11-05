import pytest
from string_utils import StringUtils


utils = StringUtils()
#Позитивные тесты 
def test_capitalize_simple():
    """Позитивный: Первая буква становится заглавной."""
    assert utils.capitalize("world") == "World"

def test_delete_space():
    """Позитивный: Удаление пробелов в начале текста."""
    assert utils.trim("   My name is Max") == "My name is Max"

def test_symbol_true():
    """Позитивный: Поиск символа в строке."""
    assert utils.contains("Russia", "R") is True

#Негативные и граничные тесты
def test_no_spaces():
    """Негативный: Поиск пробелов в начале"""
    assert utils.trim("Her name") == "Her name"

def test_symbol_false():
    """Негативный: Поиск символа,символ не найден, должен вернуться False."""
    assert utils.contains("united kingdom", "U") is False
#Тесты на дефекты
def test_several_spaces():
    """Удаление нескольких пробелов подряд."""
    assert utils.trim("    Sea") == "Sea"

def test_delete_symbol():
    """Удаление выбранных символов из слова."""
    assert utils.delete_symbol("Mars", "a") == "Mrs"

def test_delete_symbol_substring():
    """Удаление подстроки."""
    assert utils.delete_symbol("SpaceX", "X") == "Space"

def test_contains_empty_symbol():
    """Пограничный случай: поиск пустой строки."""
    assert utils.contains("TV", "") is True