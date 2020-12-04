import re

with open('4/4.input') as f:
    lines = f.read().splitlines()


def is_valid_passport(value_dict):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # Ignoring "cid"
    for key in keys:
        if key not in value_dict:
            return False
    
    #byr(Birth Year) - four digits
    if len( value_dict["byr"] ) != 4:
        return False
    #at least 1920 and at most 2002.
    if 1920 > int(value_dict["byr"]) or int(value_dict["byr"]) > 2002:
        return False
    
    #iyr(Issue Year) - four digits
    if len(value_dict["iyr"]) != 4:
        return False
    #at least 2010 and at most 2020.
    if 2010 > int(value_dict["iyr"]) or int(value_dict["iyr"]) > 2020:
        return False

    #eyr(Expiration Year) - four digits
    if len(value_dict["eyr"]) != 4:
        return False
    # at least 2020 and at most 2030.
    if 2020 > int(value_dict["eyr"]) or int(value_dict["eyr"]) > 2030:
        return False

    #hgt(Height) - a number followed by either cm or in: 
    regex_pattern = re.compile(r"(\d*)(\w*)")
    height = regex_pattern.match(value_dict["hgt"]).group(1)
    measurement = regex_pattern.match(value_dict["hgt"]).group(2)
    if measurement != "cm" and measurement != "in":
        return False
    
    #If cm, the number must be at least 150 and at most 193. 
    if measurement == "cm":
        if 150 > int(height) or int(height) > 193:
            return False
    
    # If in , the number must be at least 59 and at most 76.
    if measurement == "in":
        if 59 > int(height) or int(height) > 76:
            return False

    #hcl(Hair Color) - a  # 
    if value_dict["hcl"][0] != "#":
        return False
    # followed by exactly six characters
    if len( value_dict["hcl"][1:] ) != 6:
        return False
    # 0-9 or a-f.
    allowed_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    for char in value_dict["hcl"][1:]:
        if char not in allowed_chars:
            return False

    #ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    allowed_ecl = ["amb","blu","brn","gry","grn","hzl","oth"]
    if value_dict["ecl"] not in allowed_ecl:
        return False

    #pid(Passport ID) - a nine-digit number, including leading zeroes.
    #Check if number
    try:
        int(value_dict["pid"])
    except ValueError:
        return False
    #Check number of digits
    if len(value_dict["pid"]) != 9:
        return False
    

    #cid(Country ID) - ignored, missing or not.


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
            entries = str.split(line, " ")
            for entry in entries:
                key_value_pair = str.split(entry, ":")
                value_dict[key_value_pair[0]] = key_value_pair[1]
    if is_valid_passport(value_dict):
        num_valid_passports += 1
    print(str(num_valid_passports))


run(lines)
