import re
import sys

LINE_RE = re.compile(r'^(addx|noop)(?: (-?\d+))?')


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    cycle = 1
    register = 1
    crt = []
    for matches in (LINE_RE.match(line) for line in f):
        if cycle % 40 == 1:
            crt.append('\n')
        if (cycle - 1) % 40 in (register - 1, register, register + 1):
            crt.append('#')
        else:
            crt.append(' ')
        cycle += 1
        if matches.group(1) == 'addx':
            if cycle % 40 == 1:
                crt.append('\n')
            if (cycle - 1) % 40 in (register - 1, register, register + 1):
                crt.append('#')
            else:
                crt.append(' ')
            cycle += 1
            register += int(matches.group(2))
    print(''.join(crt))
