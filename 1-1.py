with open('1.txt') as f:
    lines = f.read().splitlines()

intlines = list(map(int, lines))

print(*intlines)

for a in intlines:
    for b in intlines:
        if a + b == 2020:
            print ( str(a) + " " + str(b) )
            print ( str( a * b ) )