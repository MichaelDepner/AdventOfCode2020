from day_8_2 import *


def test_evaluate_lines_loop():
    input = [
        ("nop", 0, False),
        ("acc", 1, False),
        ("jmp", 4, False),
        ("acc", 3, False),
        ("jmp", -3, False),
        ("acc", -99, False),
        ("acc", 1, False),
        ("jmp", -4, False),
        ("acc", 6, False)
    ]
    assert evaluate_lines(input, 0, 0) == (5,False)

def test_evaluate_lines_no_loop():
    input = [
        ("nop", 0, False),
        ("acc", 1, False),
        ("jmp", 4, False),
        ("acc", 3, False),
        ("jmp", -3, False),
        ("acc", -99, False),
        ("acc", 1, False),
        ("nop", -4, False),
        ("acc", 6, False)
    ]
    assert evaluate_lines(input, 0, 0) == (8, True)

def test_try_everything():
    input = [
        ("nop", 0, False),
        ("acc", 1, False),
        ("jmp", 4, False),
        ("acc", 3, False),
        ("jmp", -3, False),
        ("acc", -99, False),
        ("acc", 1, False),
        ("jmp", -4, False),
        ("acc", 6, False)
    ]
    assert try_everything(input) == 8