
def get_range(character, number_range):
    if character in ["F","L"]: #Front of plane or Left side returns lower half of list
        return number_range[:len(number_range)//2]
    elif character in ["B","R"]: #Back of the plane or Right side returns upper half of list
        return number_range[ (len(number_range)//2) :]

def get_seat(boarding_pass):
    rows = boarding_pass[0:7]
    seats = boarding_pass[7:10]
    row_range = list( range(0,128) )
    seat_range = list( range(0,8) )
    for character in rows:
        row_range = get_range(character, row_range)
    for character in seats:
        seat_range = get_range(character, seat_range)
    
    return row_range[0] * 8 + seat_range[0]
        

def get_highest_seat_id():
    with open('day_5/day_5.input') as f:
        lines = f.read().splitlines()
    highest_seat_id = 0
    for line in lines:
        seat_id = get_seat(line)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id

print( get_highest_seat_id() )