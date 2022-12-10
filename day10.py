import advent_of_code as aoc
import numpy as np
import pandas as pd

# Read in input
num = 10
lines = aoc.input_readlines(num)
lines = [line.replace('\n','') for line in lines]

# Input
# List of commands, tracks a register
# Lines have 2 formats
#  1. noop - takes 1 cycle, does nothing
#  2. addx V - takes 2 cycles, at the end of those regiser moves V

## PART 1
# Initialize cycle count and register x
cycle = 0
x = 1
x_values = []
for line in lines:
    if line == 'noop':
        # 1 cycle, x doesn't change
        x_values.append(x)
        cycle += 1
    else:
        # CASE line == 'addx V'
        # 2 cycles, after that x changes by V
        x_values.append(x)
        cycle +=1
        x_values.append(x)
        x += int(line.split()[1])
        cycle +=1

# Get value of special cycles
special_cycles = range(20-1,cycle-1,40)
signal_strengths = []
for i in special_cycles:
    signal_strengths.append(x_values[i]*(i+1))

print(f"Sum of signal strengths from special cycles: {sum(signal_strengths)}.")
print()
print()

## PART 2

def draw_pixel(sprite,pixel_pos):
    '''
    Compare sprite and pixel_pos, if they overlap output '#', else '.'.
    Sprite covers 3 possible pixel positions.
    '''
    if sprite in [pixel_pos-1,pixel_pos,pixel_pos+1]:
        return '#'
    else:
        return '.'

def check_pixel_pos(pixel):
    '''
    pixel positions only are from 0-39, then the next row.
    If pixel reaches 40, reset to 0.
    '''
    if pixel == 40:
        pixel = 0
    return pixel

pixel_pos = -1
sprite = 1
pixels = []
for line in lines:
    if line == 'noop':
        pixel_pos += 1
        pixel_pos = check_pixel_pos(pixel_pos)
        pixels.append(draw_pixel(sprite,pixel_pos))
    else:
        pixel_pos += 1
        pixel_pos = check_pixel_pos(pixel_pos)
        pixels.append(draw_pixel(sprite,pixel_pos))

        pixel_pos += 1
        pixel_pos = check_pixel_pos(pixel_pos)
        pixels.append(draw_pixel(sprite,pixel_pos))
        
        sprite += int(line.split()[1])


for i in range(40,241,40):
    print(''.join(pixels[i-40:i])) 
        

'''

def draw_pixel(sprite,cycle):
    if sprite in [cycle-1,cycle,cycle+1]:
        return '#'
    else:
        return '.'

def check_cycle(cycle):
    if cycle == 40:
        cycle = 0
    return cycle

cycle = 0
sprite = 1
pixels = []
for line in lines[:21]:
    print(line, ':', cycle, sprite)
    
    if line == 'noop':
        cycle += 1
        cycle = check_cycle(cycle)
        pixels.append(draw_pixel(sprite,cycle))
        print(''.join(pixels))
    else:
        cycle +=1
        cycle = check_cycle(cycle)
        pixels.append(draw_pixel(sprite,cycle))
        print(''.join(pixels))

        cycle +=1
        cycle = check_cycle(cycle)
        pixels.append(draw_pixel(sprite,cycle))
        print(''.join(pixels))
        sprite += int(line.split()[1])


'''
