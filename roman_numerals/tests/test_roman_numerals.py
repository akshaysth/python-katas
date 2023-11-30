from src.roman_numerals import from_roman, to_roman


def test_to_roman():
    assert to_roman(123)


def test_from_roman():
    assert from_roman("roman_num")
