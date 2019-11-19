import snake


def test_empty():
    assert snake.build_snake("") == ""


def test_1_char():
    assert snake.build_snake("A") == "A"


def test_2_chars():
    assert snake.build_snake("AB") == "AB\n.."


def test_9_chars():
    assert snake.build_snake("ABCDEFGHI") == \
"""ABC
HID
GFE"""

def test_10_chars():
    assert snake.build_snake("ABCDEFGHIJ") == \
"""ABCD
...E
...F
JIHG"""


def test_16_chars():
    assert snake.build_snake("ABCDEFGHIJKLMNOP") == \
"""ABCD
LMNE
KPOF
JIHG"""