import functools
import sys


NEUTRAL = 0
ORDERED = -1
UNORDERED = 1


def is_ordered(left, right) -> int:
    if isinstance(left, int):
        if isinstance(right, int):
            if left == right:
                return NEUTRAL
            if left < right:
                return ORDERED
            return UNORDERED
        # right must be a list
        return is_ordered([left], right)
    # left must be a list
    if isinstance(right, int):
        return is_ordered(left, [right])
    # right must be a list
    result = NEUTRAL
    i = 0
    while result == NEUTRAL and i < len(left):
        try:
            result = is_ordered(left[i], right[i])
        except IndexError:
            return UNORDERED
        i += 1
    if result == NEUTRAL and len(right) > len(left):
        return ORDERED
    return result


def main(f):
    packets = []
    line1 = f.readline()
    line2 = f.readline()
    while line1:
        data1 = eval(line1.strip())
        data2 = eval(line2.strip())
        packets.append(data1)
        packets.append(data2)
        f.readline()
        line1 = f.readline()
        line2 = f.readline()
    packets.append([[2]])
    packets.append([[6]])
    result = sorted(packets, key=functools.cmp_to_key(is_ordered))

    print((result.index([[2]]) + 1) * (result.index([[6]]) + 1))


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
