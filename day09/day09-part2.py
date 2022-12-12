import re
import sys
from dataclasses import dataclass

LINE_RE = re.compile(r'^([UDLR]) (\d+)')
DIRECTIONS = {
    # Each entry is a tuple of (index, sign)
    'U': (1, 1),
    'D': (1, -1),
    'L': (0, -1),
    'R': (0, 1)
}


@dataclass
class PointData:
    is_touching: bool
    x_move: int
    y_move: int


def get_point_data(point_a, point_b) -> PointData:
    # Assume that point_a and point_b are 2-item lists or tuples
    x_diff = point_a[0] - point_b[0]
    x_move = 0
    if x_diff > 0:
        x_move = 1
    elif x_diff < 0:
        x_move = -1
    y_diff = point_a[1] - point_b[1]
    y_move = 0
    if y_diff > 0:
        y_move = 1
    elif y_diff < 0:
        y_move = -1
    return PointData(
        abs(x_diff) < 2 and abs(y_diff) < 2,
        x_move,
        y_move
    )


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    visited = {(0, 0)}  # Keep track of (x, y)
    head = [0, 0]
    tails = [(0, 0) for _ in range(9)]
    # last_pos = [tuple(tail) for tail in tails]  # last_pos[-1] is last position of head
    for matches in (LINE_RE.match(line) for line in f):
        direction = matches.group(1)
        steps = int(matches.group(2))
        for _ in range(steps):
            head[DIRECTIONS[direction][0]] += DIRECTIONS[direction][1]
            pd = get_point_data(head, tails[0])
            if not pd.is_touching:
                tails[0] = (tails[0][0] + pd.x_move, tails[0][1] + pd.y_move)
            for i in range(1, len(tails)):
                pd = get_point_data(tails[i-1], tails[i])
                if not pd.is_touching:
                    tails[i] = (tails[i][0] + pd.x_move, tails[i][1] + pd.y_move)
                else:
                    break
            visited.add(tails[-1])
    print(len(visited))
