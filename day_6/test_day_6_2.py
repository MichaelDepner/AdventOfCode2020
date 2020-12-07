from day_6_2 import return_groups, remove_partial_answers_from_group, count_answers

def test_input_reading():
    with open('day_6/day_6_1_test.input') as f:
        lines = f.read().splitlines()
    assert return_groups(lines) == [(1,"abc"), (3,"abc"), (2,"abac"), (4,"aaaa"), (1,"b")]


def test_remove_partial_answers_from_group():
    groups = [(1, "abc"), (3, "abc"), (2, "abac"), (4, "aaaa"), (1, "b")]
    assert remove_partial_answers_from_group(groups) == ["abc", "", "a", "a", "b"]


def test_count_answers():
    groups = ["abc", "", "a", "a", "b"]
    assert count_answers(groups) == 6

