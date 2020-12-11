from day_9_1 import *

def test_parse_input():
    with open('day_9/day_9_1_test.input') as f:
        lines = f.read().splitlines()
    assert parse_input(lines) == [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576
    ]

def test_number_is_valid():
    input = [
        35,
        20,
        15,
        25,
        47
    ]
    assert number_is_valid(input, 40) == True
    assert number_is_valid(input, 41) == False

def test_find_first_invalid_number():
    input = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576
    ]
    assert find_first_invalid_number(input, 5) == 127
    