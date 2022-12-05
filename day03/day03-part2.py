import sys


def get_priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    priority_total = 0
    elf1 = f.readline().strip()
    while elf1:
        elf2 = f.readline().strip()
        elf3 = f.readline().strip()
        intersection = set(elf1) & set(elf2) & set(elf3)
        priority_total += get_priority(intersection.pop())
        elf1 = f.readline().strip()
    print(priority_total)
