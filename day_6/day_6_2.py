
def return_groups(input):
    group_list = []
    group_in_progress = ""
    number_of_people = 0
    for line in input:
        if line == "":
            group_list.append((number_of_people,group_in_progress))
            group_in_progress = ""
            number_of_people = 0
        else:
            group_in_progress += line
            number_of_people += 1

    group_list.append((number_of_people,group_in_progress))
    return group_list


def remove_partial_answers_from_group(group_list):
    updated_group_list = []
    for group in group_list:
        character_seen = []
        updated_group = ""
        for character in group[1]:
            if character not in character_seen:
                character_seen.append(character)
                if str.count(group[1], character) == group[0]:
                    updated_group += character
        updated_group_list.append(updated_group)
    return updated_group_list


def count_answers(group_list):
    count = 0
    for group in group_list:
        count += len(group)
    return count


with open('day_6/day_6.input') as f:
    lines = f.read().splitlines()
groups = return_groups(lines)
groups_without_duplicates = remove_partial_answers_from_group(groups)
sum_of_answers = count_answers(groups_without_duplicates)
print(sum_of_answers)
