import os
import sys
import Bio
import string
import itertools
import re

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_rear.txt'))
pairs = []
lines = list(file)
for x in range(0, len(lines), 3):
    pair = []
    pair.append(lines[x].strip('\n').split(' '))
    pair.append(lines[x+1].strip('\n').split(' '))
    pairs.append(pair)

# Inversion
def invert(a, x, y):
    bef = a[0:x]
    rev = a[x:y+1][::-1]
    aft = a[y+1:]
    # print(f"{bef} {rev} {aft}")
    return bef + rev + aft

# Reversal distance
def reversal_distance(source, target):
    inversions = []
    for x in range(0, len(target)):
        if target[x] != source[x]:
            index = source.index(target[x])
            source = invert(source, x, index)
            inversions.append([x, index, source, target])
            # print(f"Pos: [{x}:{index}] - {source[x:index+1]}")
            print(f"Source: {source} - Target: {target}")
    return inversions

# result = reversal_distance(pairs[0][0], pairs[0][1])
# print(len(result))

# Output
for pair in pairs:
    result = reversal_distance(pair[0], pair[1])
    print(len(result))


# Examples:
# 5[3 2]1 4
# 5[2 3]1 4
# 5 3 [2 1 4]
# 5 3 [4 1 2]
# [5 3 2 1 4]
# [4 1 2 3 5]
# targ  = [5, 3, 2, 1, 4]
# pair1 = [5, 2, 3, 1, 4]
# pair2 = [5, 3, 4, 1, 2]
# pair3 = [4, 1, 2, 3, 5]
# result = reversal_distance(targ, pair1)
# result = reversal_distance(targ, pair2)
# result = reversal_distance(targ, pair3)
