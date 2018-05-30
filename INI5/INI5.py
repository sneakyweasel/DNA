import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ini5.txt'))
lines = [line.rstrip('\n') for line in file]

for id, line in enumerate(lines):
    if id % 2 == 1:
        print(line)
