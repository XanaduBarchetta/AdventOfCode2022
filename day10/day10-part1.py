import re
import sys

LINE_RE = re.compile(r'^(addx|noop)(?: (-?\d+))?')
CYCLES_OF_INTEREST = (20, 60, 100, 140, 180, 220)


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    cycle = 1
    register = 1
    total_ss = 0
    for matches in (LINE_RE.match(line) for line in f):
        if cycle in CYCLES_OF_INTEREST:
            total_ss += cycle * register
        cycle += 1
        if matches.group(1) == 'addx':
            if cycle in CYCLES_OF_INTEREST:
                total_ss += cycle * register
            cycle += 1
            register += int(matches.group(2))
    print(total_ss)
