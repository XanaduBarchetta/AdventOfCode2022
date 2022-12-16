import bisect
import re
import sys
from typing import Dict

LINE_RE = re.compile(r'x=(-?\d+), y=(-?\d+)')
MIN_XY = 0
MAX_XY = 4000000
TUNING_MULTIPLIER = 4000000


def get_distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_relevant_x_values(center: tuple, y_value: int, radius: int) -> (int, int):
    x_distance_from_center = radius - abs(y_value - center[1])
    if x_distance_from_center < 1:
        raise ValueError
    return center[0] - x_distance_from_center, center[0] + x_distance_from_center


def main(f):
    sensors: Dict[tuple, int] = {}
    for sensor, beacon in (LINE_RE.findall(line.strip()) for line in f):
        sensor = (int(sensor[0]), int(sensor[1]))
        beacon = (int(beacon[0]), int(beacon[1]))
        sensors[sensor] = get_distance(sensor, beacon)

    # for x in range(MIN_XY, MAX_XY + 1):
    for row in range(MAX_XY + 1):
        row_coverage = []
        for sensor, distance in sensors.items():
            try:
                bisect.insort(row_coverage, get_relevant_x_values(sensor, row, distance))
            except ValueError:
                continue
        if row_coverage[0][0] > 0:
            print(row)  # X coordinate would be zero, so only need Y
            return
        current_max = row_coverage[0][1]
        for x_min, x_max in row_coverage[1:]:
            if x_min > current_max + 1:
                print((current_max + 1) * TUNING_MULTIPLIER + row)
                return
            current_max = max(current_max, x_max)
        if current_max < MAX_XY:
            print(TUNING_MULTIPLIER * TUNING_MULTIPLIER + row)
            return


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
