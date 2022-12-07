import advent_of_code as aoc

import pandas as pd

# Read in input
num = 7
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]

DIR_LIMIT = 100_000
MIN_NEEDED = 30_000_000
TOTAL_SPACE = 70_000_000

# Input
# lines are terminal input/output
#  if line begins with $, it's a terminal command
#  lines in between terminal commands are ls output

# Build dirs dictionary
if 'content' in locals():
    del content
pwd = []
dirs = {}
for line in lines:
    if line[0] == '$':
        # CASE line is a command, check if previous lines were ls output
        if 'content' in locals():
            # CASE previous lines were ls output,
            #  save structure and delete content variable
            dir_name = '/'.join(pwd)
            dirs[dir_name] = {}
            dirs[dir_name]['pwd'] = pwd.copy()
            dirs[dir_name]['content'] = content.copy()
            del content
    else:
        # CASE line is not a command, line is ls output
        #  append content structure variable
        content.append(line)
        continue
    # Rest of code in loop only applies to commands
    if line[:4] == '$ cd':
        # CASE line is cd command,
        #  get current directory and update pwd
        line_split = line.split()
        if line_split[-1] == '..':
            pwd.pop()
            curr_dir = pwd[-1]
        else:
            curr_dir = line_split[-1]
            pwd.append(curr_dir)
    elif line == '$ ls':
        # CASE line is ls command,
        #  initialize content variable
        content = []
        file_sizes = []
# After for loop, if content has unsaved info
#  update dirs
if 'content' in locals():
    dir_name = '/'.join(pwd)
    dirs[dir_name] = {}
    dirs[dir_name]['pwd'] = pwd.copy()
    dirs[dir_name]['content'] = content.copy()


# Go through dirs dict backwards and add dir_size info
dirs_keys = list(dirs.keys())
dirs_keys.reverse()
for idir in dirs_keys:

    if dirs[idir]['content'] == []:
        # CASE this directory is empty, size = 0
        dirs[idir]['dir_size'] = 0
        continue
    # dir_size is sum of file sizes and sum of sub directories
    content_files = [pd.to_numeric(i.split()[0]) for i in dirs[idir]['content'] if i.split()[0] != 'dir'] 
    content_dirs = [i.split()[1] for i in dirs[idir]['content'] if i.split()[0] == 'dir']
    dirs[idir]['dir_size'] = sum(content_files) + sum(dirs[idir+'/'+subdir]['dir_size'] for subdir in content_dirs)


## PART 1
dirs_keys = list(dirs.keys())
sum_small_dirs = sum(dirs[idir]['dir_size'] for idir in dirs_keys if (dirs[idir]['dir_size'] <= DIR_LIMIT))
    
print(f"Sum of 'small' directories sizes: {sum_small_dirs}.")


## PART 2
# Get amount of disk space to free up based on
#  total disk space, minimum needed for update and disk space used
max_du_needed = TOTAL_SPACE - MIN_NEEDED
du = dirs['/']['dir_size']
need_to_free_up = du - max_du_needed 

dir_to_delete = min(dirs[idir]['dir_size'] for idir in dirs_keys if (dirs[idir]['dir_size'] >= need_to_free_up))

print(f"Directory size to delete: {dir_to_delete}.")
            
