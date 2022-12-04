import advent_of_code as aoc

import pandas as pd


# Input
# Each line is a pair of section assignments - pair of elves
# Pairs are separated by a comma, section assignments by hyphens
num = 4
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]

def get_elf_assignments(line):
    elf1, elf2 = line.split(',')
    elf1_min, elf1_max = elf1.split('-')
    elf2_min, elf2_max = elf2.split('-')
    elf1 = [int(elf1_min), int(elf1_max)]
    elf2 = [int(elf2_min), int(elf2_max)]
    return elf1, elf2

def check_elf1_in_elf2(elf1,elf2):
    '''
    For Part 1, check if elf1 assignment completely encompassed by elf2.
    If so return True
    '''
    if elf1[0] >= elf2[0]:
        if elf1[1] <= elf2[1]:
            return True
    return False

def check_elf2_in_elf1(elf1,elf2):
    '''
    For Part 1, check if elf2 assignment completely encompassed by elf1
    if so return True
    '''
    if elf2[0] >= elf1[0]:
        if elf2[1] <= elf1[1]:
            return True
    return False

def check_if_any_overlap(elf1, elf2):
    '''
    For Part 2, check if there is any overlap in assignments
    '''

    # Check if any elf 1 end points in elf 2
    # A single point counts as an overlap
    # So overlap == True
    if elf1[0] in elf2:
        return True
    if elf1[1] in elf2:
        return True

    # Combine elves, sort
    # if first 2 elements of elves is either elf, NO overlap
    elves = elf1 + elf2
    elves.sort()
    if elf1 == elves[:2]:
        return False
    if elf2 == elves[:2]:
        return False
    return True


## PART 1
overlaps = 0
for line in lines:
    elf1, elf2 = get_elf_assignments(line)
    if check_elf1_in_elf2(elf1,elf2):
        overlaps += 1
    elif check_elf2_in_elf1(elf1,elf2):
        overlaps += 1

print(f"The number of overlaps is {overlaps}.")


## PART 2
overlaps = 0
for line in lines:
    elf1, elf2 = get_elf_assignments(line)
    if check_if_any_overlap(elf1, elf2):
        overlaps += 1

print(f"The number of overlaps is {overlaps}.")
