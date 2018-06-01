import os
import sys
import Bio
import string
import itertools
import re

# Read input file to vars
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lgis.txt'))
lines = file.readlines()
n = int(lines[0])
pi_perm = [int(x) for x in lines[1].split(" ")]
print(f"N: {n}")
print(f"PI: {pi_perm}")
print("------")

# https://rosettacode.org/wiki/Longest_increasing_subsequence#Python
def longest_increasing_subsequence(A):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(A)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (A[M[mid]] < A[i]):
               lo = mid+1
           else:
               hi = mid-1

       newL = lo
       P[i] = M[newL-1]
       M[newL] = i

       if (newL > L):
           L = newL

    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(A[k])
        k = P[k]
    return S[::-1]

# http://www.geekviewpoint.com/python/dynamic_programming/lds
def longest_decreasing_subsequence(A):
    m = [0] * len(A)
    for x in range( len( A ) - 2, -1, -1 ):
        for y in range( len( A ) - 1, x, -1 ):
            if m[x] <= m[y] and A[x] > A[y]:
                m[x] = m[y] + 1 # or use m[x]+=1
    max_value = max(m)

    result = []
    for i in range(len(m)):
        if max_value == m[i]:
            result.append(A[i])
            max_value -= 1

    return result


lis = longest_increasing_subsequence(pi_perm)
print(" ".join([str(num) for num in lis]))

lds = longest_decreasing_subsequence(pi_perm)
print(" ".join([str(num) for num in lds]))
