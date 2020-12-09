from day_8_1 import *

def test_parse_input_line():
    assert parse_input_line("nop +0") == ("nop",0,False)
    assert parse_input_line("jmp -3") == ("jmp",-3,False)
    assert parse_input_line("acc -99") == ("acc",-99,False)
    
def test_parse_input_lines():
    with open('day_8/day_8_1_test.input') as f:
        lines = f.read().splitlines()
    assert parse_input_lines(lines) == [
        ("nop",0,False),
        ("acc",1,False),
        ("jmp",4,False),
        ("acc",3,False),
        ("jmp",-3,False),
        ("acc",-99,False),
        ("acc",1,False),
        ("jmp",-4,False),
        ("acc",6,False)
    ]

def test_evaluate_lines():
    input = [
        ("nop",0,False),
        ("acc",1,False),
        ("jmp",4,False),
        ("acc",3,False),
        ("jmp",-3,False),
        ("acc",-99,False),
        ("acc",1,False),
        ("jmp",-4,False),
        ("acc",6,False)
    ]
    assert evaluate_lines(input,0,0) == 5