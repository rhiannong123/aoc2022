import advent_of_code as aoc

import pandas as pd

# Read in input
num = 5
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]

## PART 1

# Input
# 2 sections of input, separated by new line (separation_line_idx)
#  1. initial crate set up
#  2. instructions on moving crates
separation_line_idx = [idx for idx in range(len(lines)) if lines[idx] == ''][0]

# PARSE FIRST HALF OF INPUT - the initial stacks of crates 
# Each line here is a level in the stacks.
# Working backwards, build up stacks, using x to indicate no crate in that spot
stack_height = separation_line_idx - 1
levels = [] 
for line in reversed(lines[:stack_height]): 
    level = line.replace('    ',' x  ').replace('[','').replace(']','').replace(' ','') 
    levels.append(level)

# Get number of stacks, flatten stacks into one list,
# Reshape the flattened list into stacks.
# Basically we want to transpose - from levels get stacks
stack_count = len(level)    
flattened = [level[level_idx] for level_idx in range(stack_count) for level in levels]
idx = 0
stacks = []
for i in range(stack_count):
    istack_str = ''.join(flattened[idx:idx+stack_height]).replace('x','') 
    stacks.append(list(istack_str))      
    idx += stack_height
# stacks is now a list of lists, each sub-list is a stack

# PARSE SECOND HALF OF INPUT - the instructions
# Ex. "move 1 from 2 to 1" which gives
#  1. quantity of boxes to move
#  2. source stack location, 3. destination stack location 
instructions = lines[separation_line_idx+1:]
quantities = []
sources = []
destinations = [] 
for line in instructions:
    clean_line = line.replace('move','').replace('from','').replace('to','')
    quantity,source,destination = clean_line.split() 
    quantities.append(int(quantity))
    sources.append(int(source)-1) # python index 0
    destinations.append(int(destination)-1) # python index 0

# Go through each instruction line, use pop to move crates
#  from source stack to destination stack
for quantity,source,dest in zip(quantities,sources,destinations):
    for iquant in range(quantity): 
        if stacks[source] != []: 
            crate = stacks[source].pop() 
            stacks[dest].append(crate) 

# The top crate would be the last crate in each stack
top_crates = [istack[-1] for istack in stacks]
            
print(f"The top crates are {''.join(top_crates)}.")


## PART 2
# Input
# Reset crate stacks to initial set up
idx = 0
stacks = []
for i in range(stack_count):
    istack_str = ''.join(flattened[idx:idx+stack_height]).replace('x','') 
    stacks.append(list(istack_str))      
    idx += stack_height

# Go through each instruction line, use pop to move crates
#  from source stack to destination stack
for quantity,source,dest in zip(quantities,sources,destinations):
    # crates = crates to move
    crates = []
    for iquant in range(quantity): 
        if stacks[source] != []: 
            crates.append(stacks[source].pop())
    if crates != []:
        for icrate in reversed(crates):
            stacks[dest].append(icrate)
            
# The top crate would be the last crate in each stack
top_crates = [istack[-1] for istack in stacks]
            
print(f"The top crates are {''.join(top_crates)}.")
