from day_6_1 import return_groups, remove_duplicates_from_group, count_answers

def test_input_reading():
    with open('day_6/day_6_1_test.input') as f:
        lines = f.read().splitlines()
    assert return_groups(lines) == ["abc","abc","abac","aaaa","b"]


def test_remove_duplicates_from_group():
    groups = ["abc", "abc", "abac", "aaaa", "b"]
    assert remove_duplicates_from_group(groups) == ["abc","abc","abc","a","b"]


def test_count_answers():
    groups = ["abc", "abc", "abc", "a", "b"]
    assert count_answers(groups) == 11