import os
import sys
import heapq_max

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_hea.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(f"N: {n}")

# Process inputs
nums = [int(x) for x in lines[0].split(" ")]
print(f"NUMS: {nums}")

# Heap Max
heap_max = []
heapq_max.heapify_max(nums)

print(" ".join([str(x) for x in nums]))
