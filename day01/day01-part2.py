import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    max_cals = [0, 0, 0]  # Ordered greatest to least
    current_cals = 0
    for line in f:
        if not line.strip():
            if current_cals > max_cals[0]:
                max_cals = [current_cals, max_cals[0], max_cals[1]]
            elif current_cals > max_cals[1]:
                max_cals = [max_cals[0], current_cals, max_cals[1]]
            elif current_cals > max_cals[2]:
                max_cals = [max_cals[0], max_cals[1], current_cals]
            current_cals = 0
        else:
            current_cals += int(line.strip())
    if current_cals > max_cals[0]:
        max_cals = [current_cals, max_cals[0], max_cals[1]]
    elif current_cals > max_cals[1]:
        max_cals = [max_cals[0], current_cals, max_cals[1]]
    elif current_cals > max_cals[2]:
        max_cals = [max_cals[0], max_cals[1], current_cals]
    print(sum(max_cals))
