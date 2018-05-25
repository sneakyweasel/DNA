# A partial permutation is an ordering of only k objects taken from a collection containing n objects (i.e., k≤n). For example, one partial permutation of three of the first eight positive integers is given by (5,7,2)
# The statistic P(n,k) counts the total number of partial permutations of k objects that can be formed from a collection of n objects. Note that P(n,n) is just the number of permutations of n objects, which we found to be equal to n!=n(n−1)(n−2)⋯(3)(2) in “Enumerating Gene Orders”.
# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0
# Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import os
import sys
from itertools import permutations

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_pper.txt'))
vars = file.read()
# vars = "21 7"
n = int(vars.split(' ')[0])
k = int(vars.split(' ')[1])

# Create array
full = list(range(n, 0, -1))[0:k]
print(full)

solution = 1
for num in full:
    solution *= num

print(solution % 1000000)
