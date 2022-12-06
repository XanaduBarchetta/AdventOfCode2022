import re
import sys
from collections import defaultdict


MOVE_RE = re.compile(r'^move (?P<amount>\d+) from (?P<source>\d+) to (?P<destination>\d+)$')


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    stacks = defaultdict(list)
    stack_lines = []
    line = f.readline()[:-1]
    while not line.startswith(' 1'):
        stack_lines.append(line)
        line = f.readline()[:-1]
    for stack_line in reversed(stack_lines):
        stack = 1
        for crate in stack_line[1::4]:
            if crate != ' ':
                stacks[str(stack)].append(crate)
            stack += 1
    line = f.readline()
    for matches in (MOVE_RE.fullmatch(line.strip()) for line in f):
        amount = int(matches['amount'])
        stacks[matches['destination']].extend(stacks[matches['source']][-amount:])
        del stacks[matches['source']][-amount:]
    print(''.join(stacks[str(index+1)][-1] for index in range(len(stacks.keys()))))
