import os
import sys
from heapq import merge

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ms.txt'))
lines = [line.rstrip('\n') for line in file]

n = lines[0]
arr = [int(x) for x in lines[1].split(" ")]

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

sarr = [str(x) for x in merge_sort(arr)]
print(" ".join(sarr))
