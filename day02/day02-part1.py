"""
A | X = ROCK
B | Y = PAPER
C | Z = SCISSORS
"""
import sys


LOSS = 0
TIE = 3
WIN = 6
PLAY_SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
MATCHUP_SCORES = {
    'A': {
        'X': TIE,
        'Y': WIN,
        'Z': LOSS
    },
    'B': {
        'X': LOSS,
        'Y': TIE,
        'Z': WIN
    },
    'C': {
        'X': WIN,
        'Y': LOSS,
        'Z': TIE
    }
}


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    score = 0
    for line in f:
        their_move, my_move = line.strip().split(' ')
        score += PLAY_SCORES[my_move] + MATCHUP_SCORES[their_move][my_move]
    print(score)
