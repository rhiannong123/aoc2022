import advent_of_code as aoc

import pandas as pd


## PART 1
num = 1
lines = aoc.input_readlines(num)

# Input - each line is a number or blank.
#  make each number an integer, each blank a -1
lines = [int(line.replace('\n','')) if line != '\n' else -1 for line in lines]

elves = []
current_elf = 0
# Go thru each line, track current_total (current_elf)
#  if new line is a number, add it to the current total (current_elf)
#  if new line is a -1, done with current_elf, append elves and reset current_elf
for line in lines:
    if line == -1:
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += line

if lines[-1] != -1:
    elves.append(current_elf)


print(f"The max calories carried by any elf is {max(elves)}")    

## PART 2
elves.sort()
print(f"The calories carried by the top 3 most calorie burdened elves is {sum(elves[-3:])}")
