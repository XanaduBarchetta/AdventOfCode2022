import re
import sys
from itertools import pairwise

VERTEX_RE = re.compile(r'(?:^| )(\d+),(\d+)')
START_POINT = (500, 0)


def main(f):
    solids = set()
    max_y = 0
    # Build set of rocks
    vertices = [(int(x), int(y)) for (x, y) in VERTEX_RE.findall(f.readline())]
    while vertices:
        for a, b in pairwise(vertices):
            max_y = max(a[1], max_y)
            if a[0] == b[0]:
                # Parallel to y-axis
                for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                    solids.add((a[0], y))
            else:
                # Parallel to x-axis
                for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    solids.add((x, a[1]))
        max_y = max(vertices[-1][1], max_y)
        vertices = [(int(x), int(y)) for (x, y) in VERTEX_RE.findall(f.readline())]
    max_y += 2
    # Drop sand until it falls forever
    sand_x = START_POINT[0]
    sand_y = START_POINT[1]
    total_sand = 0
    while sand_y < max_y and START_POINT not in solids:
        if sand_y + 1 == max_y:
            solids.add((sand_x, sand_y))
            total_sand += 1
            sand_x = START_POINT[0]
            sand_y = START_POINT[1]
        elif (sand_x, sand_y + 1) not in solids:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in solids:
            sand_x += -1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in solids:
            sand_x += 1
            sand_y += 1
        else:
            solids.add((sand_x, sand_y))
            total_sand += 1
            sand_x = START_POINT[0]
            sand_y = START_POINT[1]
    print(total_sand)


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
