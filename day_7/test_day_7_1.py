from day_7.day_7_1 import *

def test_parse_input_line():
    assert parse_input_line("light red bags contain 1 bright white bag, 2 muted yellow bags.") == {"light red":[("bright white",1),("muted yellow",2)]}
    assert parse_input_line("dotted black bags contain no other bags.") == {"dotted black":[]}

def test_parse_input_lines():
    with open('day_7/day_7_1_test.input') as f:
        lines = f.read().splitlines()
    assert parse_input_lines(lines) == {
        "light red":[("bright white",1),("muted yellow",2)],
        "dark orange":[("bright white",3),("muted yellow",4)],
        "bright white":[("shiny gold",1)],
        "muted yellow":[("shiny gold",2),("faded blue",9)],
        "shiny gold":[("dark olive",1),("vibrant plum",2)],
        "dark olive":[("faded blue",3),("dotted black",4)],
        "vibrant plum":[("faded blue",5),("dotted black",6)],
        "faded blue":[],
        "dotted black":[]
        }
def test_can_be_reached():
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
    assert can_be_reached("shiny gold", dag, [("light red", 0)]) == True
    assert can_be_reached("shiny gold", dag, [("dark olive", 0)]) == False

def test_count_can_be_reached():
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
    assert count_can_be_reached("shiny gold", dag) == 4
    assert count_can_be_reached("faded blue", dag) == 7
    assert count_can_be_reached("dotted black", dag) == 7
