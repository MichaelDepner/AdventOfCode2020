from day_8_1 import parse_input_lines
from typing import List, Tuple

def evaluate_lines(list: List[Tuple[str, int, bool]], accumulator: int, index: int) -> Tuple[int,bool]:
    if index == len(list):
        return (accumulator,True)

    command = list[index][0]
    value = list[index][1]
    visited = list[index][2]

    if visited:
        return (accumulator,False)
    list[index] = (command, value, True)

    if command == "nop":
        index += 1
    elif command == "acc":
        accumulator += value
        index += 1
    elif command == "jmp":
        index += value

    return evaluate_lines(list, accumulator, index)

def try_everything(list):
    for i, entry in enumerate(list):
        list_copy = list.copy()

        if entry[0] == "nop":
            updated_entry = ("jmp",entry[1],entry[2])
            list_copy[i] = updated_entry
            result = evaluate_lines(list_copy,0,0)
            if result[1] == True:
                return result[0]

        elif entry[0] == "jmp":
            updated_entry = ("nop", entry[1], entry[2])
            list_copy[i] = updated_entry
            result = evaluate_lines(list_copy, 0, 0)
            if result[1] == True:
                return result[0]


with open('day_8/day_8.input') as f:
    lines = f.read().splitlines()
parsed_input = parse_input_lines(lines)
print(try_everything(parsed_input))