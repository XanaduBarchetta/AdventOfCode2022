import math
import sys
from queue import Queue


class Point:
    def __init__(self, elevation: str):
        self.elevation: int = Point._char_to_elevation(elevation)
        self.distance = math.inf

    @staticmethod
    def _char_to_elevation(char: str) -> int:
        if char == 'S':
            return 0
        if char == 'E':
            return 26
        return ord(char) - 97


def main(f):
    start = None
    peak = None
    hill = {}
    row = 0
    max_col = 0
    for line in f:
        max_col = len(line.strip())
        try:
            start = (row, line.index('S'))
        except ValueError:
            pass
        try:
            peak = (row, line.index('E'))
        except ValueError:
            pass
        for col, char in enumerate(line.strip()):
            hill[(row, col)] = Point(char)
        row += 1
    hill[start].distance = 0
    max_row = row
    coords = Queue()
    coords.put(start)
    while not coords.empty():
        point = coords.get()
        for (r, c) in (
            (point[0], point[1] - 1),
            (point[0], point[1] + 1),
            (point[0] - 1, point[1]),
            (point[0] + 1, point[1])
        ):
            if (
                    0 <= r < max_row and
                    0 <= c < max_col and
                    hill[(r, c)].elevation - hill[point].elevation < 2 and
                    hill[(r, c)].distance > hill[point].distance + 1
            ):
                hill[(r, c)].distance = hill[point].distance + 1
                coords.put((r, c))

    print(hill[peak].distance)


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
