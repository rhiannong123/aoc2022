import advent_of_code as aoc

import pandas as pd
import numpy as np

# Read in input
num = 11
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]



# Input
# Monkeys
monkeys = {}
for line in lines:
    line_split = line.split()
    if line_split == []:
        continue
    
    if line_split[0] == 'Monkey':
        numstr = line_split[1].replace(':','')
        monkeys[numstr] = {}
    elif line_split[0] == 'Starting':
        monkeys[numstr]['items'] = [int(i) for i in line.split(':')[1].split(',')] 
    elif line_split[0] == 'Operation:':
        monkeys[numstr]['operation'] = ''.join(line_split[1:])
    elif line_split[0] == 'Test:':
        monkeys[numstr]['test'] = int(line_split[-1])
    elif 'If true' in line:
        monkeys[numstr]['if_true'] = int(line_split[-1])
    elif 'If false' in line:
        monkeys[numstr]['if_false'] = int(line_split[-1])
        



## PART 1
inspections = [0]*len(monkeys)
for _ in range(20):
    for monkey in monkeys:
        items = monkeys[monkey]['items']
        operation = monkeys[monkey]['operation']
        test = monkeys[monkey]['test']

        for item in items:
            inspections[int(monkey)] += 1
            if '*' in operation:
                calc = operation.split('=')[1].split('*')
                calc = [item if i == 'old' else int(i) for i in calc]
                new = np.prod(calc)
                new = int(np.floor(new/3.))
            else:
                calc = operation.split('=')[1].split('+')
                calc = [item if i == 'old' else int(i) for i in calc]
                new = sum(calc)
                new = int(np.floor(new/3.))
            if new % test == 0:
                new_monkey = str(monkeys[monkey]['if_true'])
            else:
                new_monkey = str(monkeys[monkey]['if_false'])


            monkeys[new_monkey]['items'].append(new)



        monkeys[monkey]['items'] = []
            

inspections.sort()
print(f"Level of monkey business: {inspections[-1]*inspections[-2]}.")


## PART 2


monkeys = {}
for line in lines:
    line_split = line.split()
    if line_split == []:
        continue
    
    if line_split[0] == 'Monkey':
        numstr = line_split[1].replace(':','')
        monkeys[numstr] = {}
    elif line_split[0] == 'Starting':
        monkeys[numstr]['items'] = [int(i) for i in line.split(':')[1].split(',')] 
    elif line_split[0] == 'Operation:':
        monkeys[numstr]['operation'] = ''.join(line_split[1:])
    elif line_split[0] == 'Test:':
        monkeys[numstr]['test'] = int(line_split[-1])
    elif 'If true' in line:
        monkeys[numstr]['if_true'] = int(line_split[-1])
    elif 'If false' in line:
        monkeys[numstr]['if_false'] = int(line_split[-1])

inspections = [0]*len(monkeys)
for x in range(10000):
    print(x)
    for monkey in monkeys:
        items = monkeys[monkey]['items']
        operation = monkeys[monkey]['operation']
        test = monkeys[monkey]['test']

        for item in items:
            inspections[int(monkey)] += 1
            if '*' in operation:
                calc = operation.split('=')[1].split('*')
                calc = [item if i == 'old' else int(i) for i in calc]
                new = np.prod(calc)
                #new = int(np.floor(new/3.))
            else:
                calc = operation.split('=')[1].split('+')
                calc = [item if i == 'old' else int(i) for i in calc]
                new = sum(calc)
                #new = int(np.floor(new/3.))
            if new % test == 0:
                new_monkey = str(monkeys[monkey]['if_true'])
            else:
                new_monkey = str(monkeys[monkey]['if_false'])


            monkeys[new_monkey]['items'].append(new)



        monkeys[monkey]['items'] = []
            

inspections.sort()
print(f"Level of monkey business: {inspections[-1]*inspections[-2]}.")
