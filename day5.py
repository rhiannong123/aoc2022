import advent_of_code as aoc

import pandas as pd

# Read in input
num = 5
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]

## PART 1

# Input
# 2 sections of input, separated by new line
#  1. initial crate set up
#  2. instructions on moving creates
separation_line_idx = [idx for idx in range(len(lines)) if lines[idx] == ''][0]
stacks_line = lines[separation_line_idx - 1]
stack_height = separation_line_idx - 1

levels = [] 
for line in reversed(lines[:stack_height]): 
    level = line.replace('    ',' x  ').replace('[','').replace(']','').replace(' ','') 
    levels.append(level)
stack_count = len(level)
    
flattened = [level[level_idx] for level_idx in range(stack_count) for level in levels]

idx = 0
stacks = []
for i in range(stack_count):
    istack_str = ''.join(flattened[idx:idx+stack_height]).replace('x','') 
    stacks.append(list(istack_str))      
    idx += stack_height

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
    
for quantity,source,dest in zip(quantities,sources,destinations):
    for iquant in range(quantity): 
        if stacks[source] != []: 
            crate = stacks[source].pop() 
            stacks[dest].append(crate) 

top_crates = [istack[-1] for istack in stacks]
            
print(f"The top crates are {''.join(top_crates)}.")


## PART 2
for quantity,source,dest in zip(quantities,sources,destinations):
    print()
    print(quantity, source, dest)
    # crates = crates to move
    crates = []
    for iquant in range(quantity): 
        if stacks[source] != []: 
            crates.append(stacks[source].pop())
    print(crates)
    if crates != []:
        for icrate in reversed(crates):
            stacks[dest].append(icrate)
    print(stacks)
            
top_crates = [istack[-1] for istack in stacks]
            
print(f"The top crates are {''.join(top_crates)}.")
