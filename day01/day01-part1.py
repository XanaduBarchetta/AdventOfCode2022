import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    max_cals = 0
    current_cals = 0
    for line in f:
        if not line.strip():
            if current_cals > max_cals:
                max_cals = current_cals
            current_cals = 0
        else:
            current_cals += int(line.strip())
    if current_cals > max_cals:
        print(current_cals)
    else:
        print(max_cals)
