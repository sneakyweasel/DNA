import os
import sys
import random
import itertools

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lexv.txt'))
lines = file.readlines()
alphabet = lines[0].strip("\n").split(" ")
num = int(lines[1])
length = len(alphabet)
# print(f"ALP: {alphabet} - LEN: {length}")
# print(num)
# print("-----")

arr = []
for x in range(1, num+1):
    arr += list(itertools.product(range(len(alphabet)), repeat = x))
sorts = sorted(arr)
# print(sorts)

results = []
for numstr in sorts:
    strand = ""
    for c in numstr:
        strand += alphabet[c]
    results.append(strand.ljust(num, ' '))
# print(results)

for result in results:
    print(result)
