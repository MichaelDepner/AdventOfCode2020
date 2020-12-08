from day_7.day_7_2 import *


def test_count_bags():
    dag = {
        "light red": [("bright white", 1), ("muted yellow", 2)],
        "dark orange": [("bright white", 3), ("muted yellow", 4)],
        "bright white": [("shiny gold", 1)],
        "muted yellow": [("shiny gold", 2), ("faded blue", 9)],
        "shiny gold": [("dark olive", 1), ("vibrant plum", 2)],
        "dark olive": [("faded blue", 3), ("dotted black", 4)],
        "vibrant plum": [("faded blue", 5), ("dotted black", 6)],
        "faded blue": [],
        "dotted black": []
    }
    assert count_bags(dag, dag["shiny gold"], {}) == {
        'dark olive': 1, 'vibrant plum': 2, 'faded blue': 13, 'dotted black': 16}
