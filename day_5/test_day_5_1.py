import pytest
from day_5_1 import get_seat, get_range

def test_get_range_lower():
    assert get_range("F",list(range(0,128))) == list(range(0,64))
    assert get_range("F",list(range(0,64))) == list(range(0,32))
    assert get_range("F",list(range(0,1))) == list(range(0,0))
    assert get_range("F",list(range(32,64))) == list(range(32,48))
    assert get_range("R",list(range(0,8))) == list(range(4,8))

def test_get_range_upper():
    assert get_range("B",list(range(0,128))) == list(range(64,128))
    assert get_range("B",list(range(0,64))) == list(range(32,64))
    assert get_range("B",list(range(32,48))) == list(range(40,48))
    assert get_range("B",list(range(40,48))) == list(range(44,48))
    assert get_range("L",list(range(4,8))) == list(range(4,6))

#Testing the example from the task definition
def test_get_range_story():
    #Start by considering the whole range, rows 0 through 127.
    #F means to take the lower half, keeping rows 0 through 63.
    assert get_range("F",list(range(0,128))) == list(range(0,64))

    #B means to take the upper half, keeping rows 32 through 63.
    assert get_range("B",list(range(0,64))) == list(range(32,64))

    #F means to take the lower half, keeping rows 32 through 47.
    assert get_range("F",list(range(32,64))) == list(range(32,48))

    #B means to take the upper half, keeping rows 40 through 47.
    assert get_range("B",list(range(32,48))) == list(range(40,48))

    #B keeps rows 44 through 47.
    assert get_range("B",list(range(40,48))) == list(range(44,48))

    #F keeps rows 44 through 45.
    assert get_range("F",list(range(44,48))) == list(range(44,46))

    #The final F keeps the lower of the two, row 44.
    assert get_range("F",list(range(44,46))) == list(range(44,45))

    #Start by considering the whole range, columns 0 through 7.
    #R means to take the upper half, keeping columns 4 through 7.
    assert get_range("R",list(range(0,8))) == list(range(4,8))

    #L means to take the lower half, keeping columns 4 through 5.
    assert get_range("L",list(range(4,8))) == list(range(4,6))

    #The final R keeps the upper of the two, column 5.
    assert get_range("R",list(range(4,6))) == list(range(5,6))

#Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
def test_get_seat():
    assert get_seat("FBFBBFFRLR") == 357
    assert get_seat("BFFFBBFRRR") == 567
    assert get_seat("FFFBBBFRRR") == 119
    assert get_seat("BBFFBBFRLL") == 820