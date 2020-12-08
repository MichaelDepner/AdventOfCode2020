import re
from typing import List, Tuple

def parse_input_line(line):
    pattern = re.compile(r"(.*) \+?(-?\d+)")
    match = pattern.match(line)
    command = match.group(1)
    number = match.group(2)
    return (command,int(number),False)

def parse_input_lines(lines):
    commands = []
    for line in lines:
        commands.append(parse_input_line(line))
    return commands

def evaluate_lines(list: List[Tuple[str,int,bool]], accumulator: int, index: int) -> int:
    command = list[index][0]
    value = list[index][1]
    visited = list[index][2]

    if visited:
        return accumulator
    list[index] = (command, value, True)

    if command == "nop":
        index += 1
    elif command == "acc":
        accumulator += value
        index += 1
    elif command == "jmp":
        index += value

    return evaluate_lines(list, accumulator, index)

with open('day_8/day_8.input') as f:
    lines = f.read().splitlines()
parsed_input = parse_input_lines(lines)
answer = evaluate_lines(parsed_input,0,0)
print(answer)