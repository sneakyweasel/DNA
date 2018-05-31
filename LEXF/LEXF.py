import os
import sys
import random
import itertools

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lexf.txt'))
lines = file.readlines()
alphabet = lines[0].strip("\n").split(" ")
num = int(lines[1])
# print(alphabet)
# print(num)

strings = (list(itertools.product(alphabet, repeat = num)))
for string in strings:
    print("".join(string))
