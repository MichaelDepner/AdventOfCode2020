with open('2.txt') as f:
    lines = f.read().splitlines()

valid_passwords = 0

for line in lines:
    low  = int( line.split("-")[0] )
    high = int( line.split("-")[1].split(" ")[0] )
    char = line.split("-")[1].split(" ")[1].split(":")[0]
    passw = line.split(" ")[2]
    print(passw)

    number_of_char = passw.count(char)

    if low <= number_of_char and number_of_char <= high:
        valid_passwords += 1

print( str( valid_passwords ) )