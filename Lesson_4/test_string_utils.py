import pytest

from string_utils import StringUtils


string_utils = StringUtils()

# Позитивные проверки:
# 1. Заглавная буква


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("type", "Type"),
    ("hello world", "Hello world"),
    ("building_10", "Building_10"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 2. Пробелы в начале


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("123  ", "123  "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 3. Поиск символа


@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("Noise", "i") is True
    assert string_utils.contains("House 10", "1") is True
    assert string_utils.contains("2025", "2") is True
    assert string_utils.contains("Street", "w") is False
    assert string_utils.contains("2025", "q") is False
    assert string_utils.contains("20 июля 2025", "ав") is False

# 4. Удаление символа


@pytest.mark.positive
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("Hello!", "!") == "Hello"
    assert string_utils.delete_symbol("Number 200", "20") == "Number 0"

# Негативные проверки:
# 1. Заглавная буква


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 2. Пробелы в начале


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  ", ""),
    ("", ""),
    ("  0", "0"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 3. Поиск символа


@pytest.mark.negative
def test_contains_negative():
    assert string_utils.contains("Power", " ") is False
    assert string_utils.contains("00", "@") is False
    assert string_utils.contains("", "") is True
    assert string_utils.contains("(%)", "(%)") is True

# 4. Удаление символа


@pytest.mark.negative
def test_delete_symbol_negative():
    assert string_utils.delete_symbol(" ", "@") == " "
    assert string_utils.delete_symbol("Hi!", " ") == "Hi!"
    assert string_utils.delete_symbol("&*", "2") == "&*"
