import os
import sys
from itertools import permutations

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_pper.txt'))
# vars = file.read()
vars = "21 7"
n = int(vars.split(' ')[0])
k = int(vars.split(' ')[1])

# Create array
arr = list(range(1, n + 1))
pper = list(permutations(arr, k))
print(len(pper) % 1000000)
