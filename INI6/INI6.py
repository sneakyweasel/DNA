import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ini6.txt'))
# lines = [line.rstrip('\n') for line in file]
str = file.read().rstrip('\n')

dict = {}
for word in str.split(' '):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for key, value in dict.items():
    print(f"{key} {value}")
