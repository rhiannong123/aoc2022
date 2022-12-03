import advent_of_code as aoc

import pandas as pd

RANKED = '#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Input
# Each line is an elf's rucksack with 2 compartments,first half compartment 1, next 2

num = 3
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]


## PART 1
    
prioritize = 0
for line in lines:
    compsize = int(len(line)/2)
    comp1 = line[:compsize]
    comp2 = line[compsize:]

    # Get the one unique letter in both compartments (case sensitve a != A)
    shared = set(comp1).intersection(comp2)
    if len(shared) != 1:
        print('UH OH that was unexpected, only 1 character should be in both compartments')
    else:
        # Convert set to single letter string
        shared = list(shared)[0]

    # Get priority and add to current sum of prioritize
    prioritize += RANKED.find(shared)

print(f"The sum of the priorities is {prioritize}.")


## PART 2
# Group elves (elf = line) in groups of 3, find common element in each group
prioritize = 0
# For loop over each group of 3
for i in range(0,len(lines),3):
    # Get elves in group, get badge (common element in the 3 strings)
    elf1, elf2, elf3 = lines[i], lines[i+1], lines[i+2]
    badge = set(elf1).intersection(elf2).intersection(elf3)
    if len(badge) != 1:
        print('UH OH that was unexpected, only 1 character should be common amongst 3 elves.')
    else:
        # Convert set to single letter string
        badge = list(badge)[0]

    # Get priority and add to current sum of prioritize
    prioritize += RANKED.find(badge)  

print(f"The sum of the priorities is {prioritize}.")
