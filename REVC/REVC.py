import os
import sys
import platform

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_revc.txt'))
# dna = [line.rstrip('\n') for line in file][0]

# Rabbits variables
start = 2
months = 5
offstrings = 3

# Recurrence
current = start
for x in range(months):
    current = current / 2 * 3
    print(f'Month {x}! There are {current} rabits.')
