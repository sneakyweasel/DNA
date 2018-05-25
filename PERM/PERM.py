import os
import sys
from itertools import permutations

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_perm.txt'))
vars = file.read()
# vars = "4"
n = int(vars)

# Create array
arr = list(range(1, n + 1))

# Permutations
solution = list(permutations(arr))

print(len(solution))
for perm in solution:
    nums = list(perm)
    num_string = ' '.join([str(x) for x in nums])
    print(num_string)
