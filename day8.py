import advent_of_code as aoc

import pandas as pd
import math

# Read in input
num = 8
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]


def check_if_visible(df,x,y):

    tree = df.iloc[x,y]
    
    up = df.iloc[:x,y].to_list()
    down = df.iloc[x+1:,y].to_list()
    left = df.iloc[x,:y].to_list()
    right = df.iloc[x,y+1:].to_list()

    sight_lines = [up,down,left,right]

    if any(sight_line == [] for sight_line in sight_lines):
        # CASE is on edge, VISIBLE
        return True
    
    for sight_line in sight_lines:
        if all(tree > sight_line):
            return True

    return False


def get_scenic_score(df,x,y):

    tree = df.iloc[x,y]
    
    up = df.iloc[:x,y].to_list()
    down = df.iloc[x+1:,y].to_list()
    left = df.iloc[x,:y].to_list()
    right = df.iloc[x,y+1:].to_list()
    # Want to order up, left where first element is closest to tree spot
    up.reverse()
    left.reverse()

    sight_lines = [up,down,left,right]

    if any(sight_line == [] for sight_line in sight_lines):
        # CASE is on edge, scenic_score = 0
        return 0
    
    viewing_scores = []
    for sight_line in sight_lines:
        # Get viewing_levels of each tree along sight_line
        #  list comparing tree to trees along sight_line
        viewing_levels = [tree - i for i in sight_line]

        # Count up number of trees that are visible from current tree
        # Stop if a tree of same height or taller found
        keep_going = 1
        viewing_score = 0
        for i in viewing_levels:

            if keep_going == 0:
                continue
            
            if i > 0:
                viewing_score += 1
            else:
                viewing_score += 1
                keep_going = 0
        viewing_scores.append(viewing_score)

    # Return product
    return math.prod(viewing_scores)


# Input
# Turn into a grid - df of integers
df = pd.DataFrame([list(line) for line in lines])
df = df.apply(pd.to_numeric)

## PART 1
# Create a df where 1 means visible from the edge, 0 if not
dfvisible = df.copy()*0
for x in df.index:
    for y in range(len(df.columns)):
        
        if check_if_visible(df,x,y):
            dfvisible.iloc[x,y] = 1
        
print(f"Number of visible trees: {dfvisible.sum().sum()}.")


## PART 2
# Create a df where each entry is the viewing score for that tree
dfscore = df.copy()*0
for x in df.index:
    for y in range(len(df.columns)):
        
        dfscore.iloc[x,y] = get_scenic_score(df,x,y)

print(f"Highest possible scenic score: {dfscore.max().max()}.")
            
