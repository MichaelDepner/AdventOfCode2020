#from day_7.day_7_1 import parse_input_lines
from day_7_1 import parse_input_lines

def count_bags(dag, stack, parsed_dict):
    if stack == []:
        return parsed_dict
    else:
        new_stack = []
        for item in stack:
            if item[0] in parsed_dict:
                parsed_dict[item[0]] += item[1]
            else:
                parsed_dict[item[0]] = item[1]
            new_stack = new_stack + (dag[item[0]] * item[1])
        return count_bags(dag, new_stack, parsed_dict)

def run():
    with open('day_7/day_7.input') as f:
        lines = f.read().splitlines()
    dag = parse_input_lines(lines)
    bag_dict = count_bags(dag, dag["shiny gold"], {})
    return sum(bag_dict.values())

print(run())
