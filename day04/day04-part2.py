import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    contained_ranges = 0
    for range1, range2 in (line.strip().split(',') for line in f):
        r1start, r1end = (int(x) for x in range1.split('-'))
        r2start, r2end = (int(x) for x in range2.split('-'))
        if r1start <= r2start <= r1end or \
                r1start <= r2end <= r1end or \
                r2start <= r1start <= r2end or \
                r2start <= r1end <= r2end:
            contained_ranges += 1
    print(contained_ranges)
