from day_9_1 import parse_input, find_first_invalid_number
from typing import List

def find_contiguous_set(number_list: List[int], invalid_numer: int) -> List[int]:
    set: List[int] = []
    for number in number_list:
        set.append(number)
        if sum(set) == invalid_numer:
            return set
        elif sum(set) > invalid_numer:
            return find_contiguous_set(number_list[1:], invalid_numer)        

def add_min_max(set: List[int]) -> int:
    return min(set) + max(set)

with open('day_9/day_9.input') as f:
    lines = f.read().splitlines()
parsed_input = parse_input(lines)
first_invalid_number = find_first_invalid_number(parsed_input, 25)
contiguous_set = find_contiguous_set(parsed_input,first_invalid_number)
print(add_min_max(contiguous_set))
