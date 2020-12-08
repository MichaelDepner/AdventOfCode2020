import re
from typing import List, Tuple

def parse_input_line(line):
    parent_pattern = re.compile(r"(.*)(?= bags contain)")
    parent = parent_pattern.match(line).group(1)
    child_pattern = re.compile(r"(\d)(?: )(.*?)(?: bag)")
    children = child_pattern.findall(line)
    children_with_ints = list( map(lambda x: (x[1],int(x[0])), children) )
    return {parent:children_with_ints}

def parse_input_lines(lines):
    dag = {}
    for line in lines:
        dag.update( parse_input_line(line) )
    return dag


def can_be_reached(color: str, dag: dict, stack) -> bool:
    if color in dict(stack):
        return True
    elif stack == []:
        return False
    else:
        new_stack = []
        for item in stack:
            new_stack= new_stack + dag[item[0]] #append(dag[item[0]])
        return can_be_reached(color, dag, new_stack)

def count_can_be_reached(color: str, dag: dict) -> int:
    count = 0
    for node in dag.items():
        if node == color:
            break
        if can_be_reached(color, dag, node[1]):
            count += 1
    return count

def run():
    with open('day_7/day_7.input') as f:
        lines = f.read().splitlines()
    dag = parse_input_lines(lines)
    return count_can_be_reached("shiny gold", dag)

print(run())
