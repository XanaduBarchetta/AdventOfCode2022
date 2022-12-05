import sys


def get_priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    priority_total = 0
    for line in f:
        line = line.strip()
        compartment1 = set(char for char in line[:len(line)//2])
        compartment2 = set(char for char in line[len(line)//2:])
        common_item = compartment1 & compartment2
        priority_total += get_priority(common_item.pop())
    print(priority_total)
