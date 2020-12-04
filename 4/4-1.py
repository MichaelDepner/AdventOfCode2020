
with open('4/4.input') as f:
    lines = f.read().splitlines()

def is_valid_passport(value_dict):
    keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] #Ignoring "cid"
    for key in keys:
        if key not in value_dict:
            return False
    return True

def run(input):
    value_dict = {}
    num_valid_passports = 0
    for line in input:
        if line == "":
            if is_valid_passport(value_dict):
                num_valid_passports += 1
            value_dict = {}
        else:
            entries = str.split(line," ")
            for entry in entries:
                key_value_pair = str.split(entry,":")
                value_dict[key_value_pair[0]] = key_value_pair[1]
    if is_valid_passport(value_dict):
        num_valid_passports += 1
    print(str(num_valid_passports))

run(lines)
