import sys


class Tree:
    def __init__(self, height: int, visible: bool = True):
        self.height = height
        self.visible = visible

    def __str__(self):
        # For clearer debugging
        return f"{self.height} {self.visible}"


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # dimensions are [row][column]
    trees = [[Tree(height=int(char)) for char in line] for line in (line.strip() for line in f)]

    for row in range(1, len(trees)-1):
        for col in range(1, len(trees[row])-1):
            if [tree for tree in trees[row][:col] if tree.height >= trees[row][col].height] and \
                    [tree for tree in trees[row][col + 1:] if tree.height >= trees[row][col].height] and \
                    [tree for tree in (subrow[col] for subrow in trees[:row])
                     if tree.height >= trees[row][col].height] and \
                    [tree for tree in (subrow[col] for subrow in trees[row+1:])
                     if tree.height >= trees[row][col].height]:
                trees[row][col].visible = False

    print(sum(1 for row in trees for tree in row if tree.visible))
