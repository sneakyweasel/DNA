import os
import sys
import heapq_max

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ps.txt'))
lines = [line.rstrip('\n') for line in file]

# Gather variables
n = int(lines[0])
k = int(lines[2])
print(f"N: {n} - K: {k}")

# Process inputs
nums = [int(x) for x in lines[1].split(" ")]
print(f"NUMS: {nums}")

# Heap Max
nums = sorted(nums)[:k]

print(" ".join([str(x) for x in nums]))
