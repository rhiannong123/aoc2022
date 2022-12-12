import advent_of_code as aoc

import pandas as pd

# Read in input
num = 9
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]



# Input
# Path instructions



## PART 1
head = [0,0]
tail = [0,0]
tails = [tail]
for line in lines:
    print(line)
    print(f'head {head}, tail {tail}')
    direction, magnitude = line.split()
    magnitude = int(magnitude)

    i,j = head
    if direction == 'R':
        steps = [[i+mag, j] for mag in range(1,magnitude+1)]
    elif direction == 'L':
        steps = [[i-mag, j] for mag in range(1,magnitude+1)]
    elif direction == 'U':
        steps = [[i, j+mag] for mag in range(1,magnitude+1)]
    else:
        steps = [[i, j-mag] for mag in range(1,magnitude+1)]

    for step_ind,step in enumerate(steps):
        if max(abs(step[0] - tail[0]), abs(step[1] - tail[1])) == 2:
            if step_ind == 0:
                tail = head.copy()
            else:
                tail = steps[step_ind-1].copy()
            if (tail in tails) == False:
                tails.append(tail)
        print(step,tail)


    head = steps[-1]        
    print('=====================================')

print(f"Number of unique tail positions: {len(tails)}.")


## PART 2
knots = [[0,0]]*10
tails = [knots[-1]]
for line in lines:
    print(line)
    print(f'head {knots[0]}, tail {knots[9]}')
    direction, magnitude = line.split()
    magnitude = int(magnitude)

    i,j = knots[0]
    if direction == 'R':
        steps = [[i+mag, j] for mag in range(1,magnitude+1)]
    elif direction == 'L':
        steps = [[i-mag, j] for mag in range(1,magnitude+1)]
    elif direction == 'U':
        steps = [[i, j+mag] for mag in range(1,magnitude+1)]
    else:
        steps = [[i, j-mag] for mag in range(1,magnitude+1)]

    for step_ind,step in enumerate(steps):

        for knot_ind, knot in enumerate(knots):
            #print(knot_ind,knot)
                    
            if knot_ind == 0:
                print(knot_ind, knot,knots[knot_ind])
                previous_knots = knots.copy()
                knots[0] = step
            else:
                print(knot_ind, knot,knots[knot_ind])
                if max(abs(knot[0] - knots[knot_ind-1][0]), abs(knot[1] - knots[knot_ind-1][1])) == 2:
                    knots[knot_ind] = previous_knots[knot_ind-1].copy()

            if (knots[-1] in tails) == False:
                tails.append(knots[-1])

        print(step,knots)
        print('=====================================')
        


print(f"Number of unique tail positions: {len(tails)}.")

