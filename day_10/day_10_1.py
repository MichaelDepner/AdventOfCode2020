

from typing import Dict, List


def parse_input(lines):
    number_list = []
    for line in lines:
        number_list.append(int(line))
    return number_list

def parse_list(list: List[int]) -> dict:
    jolt_diff_dict = {}
    list.append(0)
    list.sort()
    for idx, number in enumerate(list):
        if idx+1 == len(list):
            diff = str( max(list)+3 - number )
        else:
            diff = str( list[idx+1] - number )

        if diff in jolt_diff_dict:
            jolt_diff_dict[diff] += 1
        else:
            jolt_diff_dict[diff] = 1
    return jolt_diff_dict

def get_jolt_multiplier(dict):
    return dict["1"] * dict["3"]

with open('day_10/day_10.input') as f:
    lines = f.read().splitlines()
parsed_input = parse_input(lines)
jolt_dict = parse_list(parsed_input)
multiplied = get_jolt_multiplier(jolt_dict)
print(multiplied)
