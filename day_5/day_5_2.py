from day_5_1 import get_seat

def get_all_seat_ids(lines):
    seat_ids = []
    for line in lines:
        seat_ids.append(get_seat(line))
    return seat_ids

def eliminate_ids(id_list, range):
    return set(range) - set(id_list)

def run():
    with open('day_5/day_5.input') as f:
        lines = f.read().splitlines()
    seat_ids = get_all_seat_ids(lines)
    id_range = list(range(min(seat_ids),max(seat_ids)+1) )
    print( eliminate_ids(seat_ids, id_range) )

run()