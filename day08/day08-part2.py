import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # dimensions are [row][column]
    trees = [[int(char) for char in line] for line in (line.strip() for line in f)]
    max_score = 0

    for row in range(1, len(trees)-1):
        for col in range(1, len(trees[row])-1):
            # Left
            left_score = 0
            for tree in reversed(trees[row][:col]):
                left_score += 1
                if tree >= trees[row][col]:
                    break
            # Right
            right_score = 0
            for tree in trees[row][col+1:]:
                right_score += 1
                if tree >= trees[row][col]:
                    break
            # Up
            up_score = 0
            for tree in (subrow[col] for subrow in reversed(trees[:row])):
                up_score += 1
                if tree >= trees[row][col]:
                    break
            # Down
            down_score = 0
            for tree in (subrow[col] for subrow in trees[row+1:]):
                down_score += 1
                if tree >= trees[row][col]:
                    break
            max_score = max(max_score, left_score * right_score * up_score * down_score)

    print(max_score)
