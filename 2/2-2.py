with open('2/2.input') as f:
    lines = f.read().splitlines()

valid_passwords = 0

for line in lines:
    low  = int( line.split("-")[0] )
    high = int( line.split("-")[1].split(" ")[0] )
    char = line.split("-")[1].split(" ")[1].split(":")[0]
    passw = line.split(" ")[2]

    if bool(passw[low-1] == char) ^ bool(passw[high-1] == char): # if left side XOR right side
        valid_passwords += 1

print( str( valid_passwords ) )