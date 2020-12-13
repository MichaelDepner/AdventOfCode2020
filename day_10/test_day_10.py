from day_10_1 import *

def test_parse_input():
    with open('day_10/day_10_1_test.input') as f:
        lines = f.read().splitlines()
    assert parse_input(lines) == [16,10,15,5,1,11,7,19,6,12,4]
    with open('day_10/day_10_1_test_2.input') as f:
        lines = f.read().splitlines()
    assert parse_input(lines) == [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

def test_parse_list():
    list = [16,10,15,5,1,11,7,19,6,12,4]
    assert parse_list(list) == {"1":7,"3":5}
    list2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
    assert parse_list(list2) == {"1":22,"3":10}

def test_get_jolt_multiplier():
    parsed_list = {"1":7,"3":5}
    assert get_jolt_multiplier(parsed_list) == 35
    parsed_list2 = {"1":22,"3":10}
    assert get_jolt_multiplier(parsed_list2) == 220
