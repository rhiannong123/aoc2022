import advent_of_code as aoc

import pandas as pd


SCORES_FOR_CHOICE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

WINNER = {
    'rock': 'paper',
    'scissors': 'rock',
    'paper': 'scissors',
}
LOSER = dict((v,k) for k,v in WINNER.items())

def get_rps_opponent(choice):
    '''
    Input of A, B, C = rock, paper, scissors respectively
    '''
    if choice.upper() == 'A':
        return 'rock'
    elif choice.upper() == 'B':
        return 'paper'
    elif choice.upper() == 'C':
        return 'scissors'
    else:
        print('choice given was not A, B or C, try again.')
        return 'None'
    
def get_rps_me(choice):
    '''
    For Part 1:
    Input of X, Y, Z = rock, paper, scissors respectively
    '''
    if choice.upper() == 'X':
        return 'rock'
    elif choice.upper() == 'Y':
        return 'paper'
    elif choice.upper() == 'Z':
        return 'scissors'
    else:
        print('choice given was not X, Y or Z, try again.')
        return 'None'


def get_score(them, me):
    '''
    For Part 1: return score. Score is based on choice and who won
     1. (1 pt for rock, 2 for paper, 3 for scissors)
     2. 0, 3 or 6 pts for loss, draw, win
    
    Input: them = their choice of rock paper scissors
           me = my choice of rock paper scissors
    '''
    # initial score based on my choice
    score = SCORES_FOR_CHOICE[me]
    # Get their choice that would defeat my choice
    choice_that_defeats_me = WINNER[me]
    
    if them == me:
        # it's a draw, add 3 to score
        return score + 3
    elif them == choice_that_defeats_me:
        # They win, add 0 to score
        return score
    else:
        # I win, add 6 to score
        return score + 6

def get_my_choice(them, outcome):
    '''
    For Part 2: get my choice based on their choice and the given outcome

    Input: them = their choice of rock paper scissors
           outcome = X,Y,Z == 'lose', 'draw', 'win'

    Example: they choose scissors and I should lose ==> return paper
    '''

    if outcome == 'Y':
        # draw - I should match them
        return them
    elif outcome == 'X':
        # lose - they should beat me
        return LOSER[them]
    else:
        # win
        return WINNER[them]
        
    
    
## PART 1
    
num = 2
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]
    
# Input
# Each line is 2 letters with a space in between
# Convert input to rock, paper, scissors for them and me
them = []
me = []
for line in lines:
    them.append(get_rps_opponent(line[0]))
    me.append(get_rps_me(line[-1]))

# Add up total score
total_score = 0
for ithem, ime in zip(them,me):
    total_score += get_score(ithem,ime)

print(f'My total score is {total_score}.')

            
    
## PART 2

num = 2
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]
    
# Input
# Each line is 2 letters with a space in between
# Convert first character  to rock, paper, scissors ==> list called them
# Second character to list called outcome
them = []
outcome = []
for line in lines:
    them.append(get_rps_opponent(line[0]))
    outcome.append(line[-1])


    
# X = Lose, Y = Draw, Z = Win
# Need to get my choice based on that and opponent choice
total_score = 0
for ithem, ioutcome in zip(them,outcome):
    # Get my choice
    ime = get_my_choice(ithem,ioutcome)
    # Get my score based on their choice and my choice
    total_score += get_score(ithem,ime)
    
print(f'My total score is {total_score}.')
