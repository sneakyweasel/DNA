import os
import sys
import bisect

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_bins.txt'))
lines = [line.rstrip('\n') for line in file]

n = lines[0]
m = lines[1]
arr1 = [int(x) for x in lines[2].split(" ")]
arr2 = [int(x) for x in lines[3].split(" ")]

results = []
for num in arr2:
    index = str(arr1.index(num) + 1) if num in arr1 else "-1"
    results.append(index)

print(" ".join(results))
