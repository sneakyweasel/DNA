import os
import sys
import bisect
from collections import Counter

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_maj.txt'))
lines = [line.rstrip('\n') for line in file]

vars = lines.pop(0)
k = vars.split(" ")[0]
n = vars.split(" ")[1]

arr = []
for line in lines:
    arr.append( [int(x) for x in line.split(" ")] )
print(arr)

results = []
for x in arr:
    most_comm = list(Counter(x).most_common(1)[0])
    if most_comm[1] > len(x) / 2:
        results.append(most_comm[0])
    else:
        results.append(-1)

str_res = [str(x) for x in results]
print(" ".join(str_res))
