import os
import sys
import itertools

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_iev.txt'))
lines = [line.rstrip('\n') for line in file]
types_num = [int(x) for x in lines[0].split(' ')]

dominant =    types_num[0]          \
            + types_num[1]          \
            + types_num[2]          \
            + .75 * types_num[3]    \
            + .5  * types_num[4]

print(int(dominant * 2))
