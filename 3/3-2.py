import math

with open('3/3.input') as f:
    lines = f.read().splitlines()

def traverse(input, right, down):
    width_of_input = len( input[0] )
    width_reached = len(input) * right
    extend_input_by = int( math.ceil( width_reached / width_of_input ) )
    extended_lines = list( map(lambda x: x*extend_input_by, input) )

    count = 0
    for i in range( 0, int( len( extended_lines ) / down ) ):
        character = extended_lines[i*down][i*right]
        if (character == "#"):
            count += 1
    return count

def run(input):
    a = traverse(input, 1, 1)
    b = traverse(input, 3, 1)
    c = traverse(input, 5, 1)
    d = traverse(input, 7, 1)
    e = traverse(input, 1, 2)
    multiplied = a*b*c*d*e
    print( str(multiplied) )

run(lines)