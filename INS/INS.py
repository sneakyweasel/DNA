import os
import sys
import bisect

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ins.txt'))
lines = [line.rstrip('\n') for line in file]

n = lines[0]
arr = [int(x) for x in lines[1].split(" ")]

def insertion_sort(l):
    swaps = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
           swaps += 1
        l[j+1] = key
    return swaps

print(insertion_sort(arr))
