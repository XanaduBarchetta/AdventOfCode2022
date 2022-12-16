import re
import sys
from typing import Iterator

LINE_RE = re.compile(r'x=(-?\d+), y=(-?\d+)')
TARGET_Y = 2000000


def distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_relevant_x_values(center: tuple, y_value: int, radius: int) -> Iterator[int]:
    x_distance_from_center = radius - abs(y_value - center[1])
    for x in range(-1 * x_distance_from_center, x_distance_from_center + 1):
        yield center[0] + x


def main(f):
    unoccupied_points = set()
    for sensor, beacon in (LINE_RE.findall(line.strip()) for line in f):
        sensor = (int(sensor[0]), int(sensor[1]))
        beacon = (int(beacon[0]), int(beacon[1]))
        for x in get_relevant_x_values(sensor, TARGET_Y, distance(sensor, beacon)):
            if beacon != (x, TARGET_Y):
                unoccupied_points.add((x, TARGET_Y))
    print(len(unoccupied_points))


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
