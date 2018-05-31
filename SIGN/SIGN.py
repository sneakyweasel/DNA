import os
import sys
import itertools

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sign.txt'))
vars = file.read()
n = int(vars)
n = 5

arr = []
for x in range(1, n+1):
    arr.append(x)
    arr.append(-x)

# Permutations
perms = list(itertools.permutations(arr, n))

# Filter
filtered = []
for perm in perms:
    temp = []
    for x in perm:
        temp.append(abs(x))
    if len(list(set(temp))) == n:
        filtered.append(perm)

# Output
print(len(filtered))
for perm in filtered:
    nums = list(perm)
    num_string = ' '.join([str(x) for x in nums])
    print(num_string)
