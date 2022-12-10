import re
import sys


LINE_RE = re.compile(r'^([UDLR]) (\d+)')
DIRECTIONS = {
    # Each entry is a tuple of (index, sign)
    'U': (1, 1),
    'D': (1, -1),
    'L': (0, -1),
    'R': (0, 1)
}


def is_touching(point_a, point_b) -> bool:
    # Assume that point_a and point_b are 2-item lists or tuples
    if abs(point_a[0] - point_b[0]) < 2 and abs(point_a[1] - point_b[1]) < 2:
        return True
    return False


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    visited = {(0, 0)}  # Keep track of (x, y)
    head = [0, 0]
    tail = (0, 0)
    head_last = tuple(head)
    for matches in (LINE_RE.match(line) for line in f):
        direction = matches.group(1)
        steps = int(matches.group(2))
        for _ in range(steps):
            head[DIRECTIONS[direction][0]] += DIRECTIONS[direction][1]
            if not is_touching(head, tail):
                tail = head_last
                visited.add(tail)
            head_last = tuple(head)
    print(len(visited))
