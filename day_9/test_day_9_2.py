from day_9_2 import *

def test_find_contiguous_set():
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
    assert find_contiguous_set(input, 127) == [15,25,47,40]

def test_add_min_max():
    contiguous_set = [15,25,47,40]
    assert add_min_max(contiguous_set) == 62
    