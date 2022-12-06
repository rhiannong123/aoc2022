import advent_of_code as aoc

import pandas as pd

# Read in input
num = 6
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]


def get_start_idx(line,number):
    '''
    Function to get first index of a unique character string of length number
    Input:
        line - input character string
        number - length of substring that we are looking for
    Output:
        integer index
    '''
    number_less_1 = number - 1 # python index 0
    
    start_idx = -1
    for idx in range(number_less_1,len(line)):
        # If start_idx already found, skip rest of character string
        if start_idx != -1:
            continue

        # Get current substring to test
        # Compare length of substring to number of unique characters
        #  if equal, we found our unique string, save idx
        possible_start = line[idx-number_less_1:idx+1]
        if len(set(possible_start)) == number:
            start_idx = idx 

    return start_idx
    

## PART 1

# Input
# A single line (test input has several examples hence 5 lines)
line = lines[0]

NUM_OF_DISTINCT_CHAR = 4
start_idx = get_start_idx(line, NUM_OF_DISTINCT_CHAR)
print(f"The first start-of-packet marker is this many characters from start of stream: {start_idx+1}.")


## PART 2
NUM_OF_DISTINCT_CHAR = 14
start_idx = get_start_idx(line, NUM_OF_DISTINCT_CHAR)
print(f"The first start-of-packet marker is this many characters from start of stream: {start_idx+1}.")
            
