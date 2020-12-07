import re


def parse_input_line(line):
    parent_pattern = re.compile(r"(.*)(?= bags contain)")
    parent = parent_pattern.match(line).group(1)
    child_pattern = re.compile(r"(\d)(?: )(.*?)(?: bag)")
    children = child_pattern.findall(line)
    children_with_ints = list( map(lambda x: (x[1],int(x[0])), children) )
    return {parent:children_with_ints}

def parse_input_lines(lines):
    dag = {}
    for line in lines:
        dag.update( parse_input_line(line) )
    return dag