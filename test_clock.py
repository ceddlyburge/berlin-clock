import pytest
#import main
from .main import *

# def inc(x):
#     return x + 1

# def test_even_seconds():
#     assert "Y" == get_seconds(2)

# def test_odd_seconds():
#     assert "O" == get_seconds(1)


# def test_5_hours_0():
#     assert "OOOO" == get_five_hours(0)

# def test_5_hours_5():
#     assert "ROOO" == get_five_hours(5)

# def test_5_hours_10():
#     assert "RROO" == get_five_hours(10)

# def test_5_hours_15():
#     assert "RRRO" == get_five_hours(15)

# def test_5_hours_20():
#     assert "RRRR" == get_five_hours(20)

# def test_5_hours_24():
#     assert "RRRR" == get_five_hours(24)


# def test_hours_0():
#     assert "OOOO" == get_hours(0)

# def test_hours_1():
#     assert "ROOO" == get_hours(1)

# def test_hours_2():
#     assert "RROO" == get_hours(2)

# def test_hours_3():
#     assert "RRRO" == get_hours(3)

# def test_hours_4():
#     assert "RRRR" == get_hours(4)

# def test_5_minutes_0():
#     assert "OOOOOOOOOOO" == get_five_minutes(0)

# def test_5_minutes_6():
#     assert "YOOOOOOOOOO" == get_five_minutes(6)

# def test_5_minutes_17():
#     assert "YYYOOOOOOOO" == get_five_minutes(17)

# def test_5_minutes_23():
#     assert "YYYYOOOOOOO" == get_five_minutes(23)

# def test_5_minutes_36():
#     assert "YYYYYYYOOOO" == get_five_minutes(36)

# def test_5_minutes_42():
#     assert "YYYYYYYYOOO" == get_five_minutes(42)

# def test_5_minutes_56():
#     assert "YYYYYYYYYYY" == get_five_minutes(56)

# def test_minutes_0():
#     assert "OOOO" == get_minutes(0)

# def test_minutes_1():
#     assert "YOOO" == get_minutes(1)

# def test_minutes_2():
#     assert "YYOO" == get_minutes(2)

# def test_minutes_3():
#     assert "YYYO" == get_minutes(3)

# def test_minutes_4():
#     assert "YYYY" == get_minutes(4)

def test_get_clock():
    assert ["O","RROO","RROO","YYYYYYYYYYY","YOOO"] == get_clock("12:56:01")

