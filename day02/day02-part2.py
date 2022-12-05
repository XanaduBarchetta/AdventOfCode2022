"""
A | X = ROCK
B | Y = PAPER
C | Z = SCISSORS
"""
import sys


LOSS = 0
TIE = 3
WIN = 6
RESULT_SCORES = {
    'X': LOSS,
    'Y': TIE,
    'Z': WIN
}
PLAY_SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
MATCHUP_PLAYS = {
    'A': {
        TIE: 'X',
        WIN: 'Y',
        LOSS: 'Z'
    },
    'B': {
        LOSS: 'X',
        TIE: 'Y',
        WIN: 'Z'
    },
    'C': {
        WIN: 'X',
        LOSS: 'Y',
        TIE: 'Z'
    }
}


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    score = 0
    for line in f:
        their_move, my_move = line.strip().split(' ')
        score += RESULT_SCORES[my_move] + PLAY_SCORES[MATCHUP_PLAYS[their_move][RESULT_SCORES[my_move]]]
    print(score)
