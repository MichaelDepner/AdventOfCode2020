from typing import List
from itertools import combinations

def parse_input(lines):
    number_list = []
    for line in lines:
        number_list.append(int(line))
    return number_list

def number_is_valid(number_list: List[int], number: int) -> bool:
    all_combinations = combinations(number_list, 2)
    sums = map(lambda x: x[0]+x[1], all_combinations )
    return number in sums

def find_first_invalid_number(number_list: List[int], preamble_length: int) -> int:
    preamble = number_list[0:preamble_length]
    number_to_check = number_list[preamble_length]
    if not number_is_valid(preamble, number_to_check):
        return number_to_check

    new_list = number_list[1:]
    return find_first_invalid_number(new_list, preamble_length)

with open('day_9/day_9.input') as f:
    lines = f.read().splitlines()
parsed_input = parse_input(lines)
result = find_first_invalid_number(parsed_input, 25)
print(result)
