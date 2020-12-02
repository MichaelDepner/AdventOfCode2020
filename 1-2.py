with open('1.txt') as f:
    lines = f.read().splitlines()

intlines = list(map(int, lines))

print(*intlines)

for a in intlines:
    for b in intlines:
        for c in intlines:
            if a + b + c == 2020:
                print ( str(a) + " " + str(b) + " " + str(c) )
                print ( str( a * b * c ) )