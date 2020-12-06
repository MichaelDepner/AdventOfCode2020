from day_5_1 import get_highest_seat_id, get_seat

def eliminate_ids(id_list):
    with open('day_5/day_5.input') as f:
        lines = f.read().splitlines()
    for line in lines:
        seat_id = get_seat(line)
        id_list.remove(seat_id)
    return id_list

id_range = list( range(0,get_highest_seat_id()+1) )
print( eliminate_ids(id_range) )