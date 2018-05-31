import os
import sys
import random
import itertools

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lexv.txt'))
lines = file.readlines()
alphabet = lines[0].strip("\n").split(" ")
alphabet.append(" ")
num = int(lines[1])
# print(alphabet)
# print(num)

arr = []
for x in range(1, num+1):
    strings = (list(itertools.product(alphabet, repeat = x)))
    for string in strings:
        arr.append("".join(string))
print(arr)
