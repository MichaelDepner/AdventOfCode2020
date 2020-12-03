import math

with open('3/3.input') as f:
    lines = f.read().splitlines()

def run(input):
    width_of_input = len( lines[0] )
    width_reached = len(lines) * 3
    extend_input_by = int( math.ceil( width_reached / width_of_input ) )
    extended_lines = list( map(lambda x: x*extend_input_by, lines) )

    count = 0
    for idx,line in enumerate(extended_lines):
        character = line[idx*3]
        if (character == "#"):
            count += 1

    print(str(count))


run(lines)