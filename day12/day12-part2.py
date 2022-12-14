import math
import sys
from queue import Queue


class Point:
    def __init__(self, elevation: str):
        self.elevation: int = Point._char_to_elevation(elevation)
        self.distance = 0 if self.elevation == 0 else math.inf

    @staticmethod
    def _char_to_elevation(char: str) -> int:
        if char == 'S':
            return 0
        if char == 'E':
            return 26
        return ord(char) - 97


def main(f):
    peak = None
    hill = {}
    row = 0
    max_col = 0
    coords = Queue()
    for line in f:
        max_col = len(line.strip())
        try:
            peak = (row, line.index('E'))
        except ValueError:
            pass
        for col, char in enumerate(line.strip()):
            hill[(row, col)] = Point(char)
            if hill[(row, col)].distance == 0:
                coords.put((row, col))
        row += 1
    max_row = row
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
