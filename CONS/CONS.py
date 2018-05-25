import os
import sys
import string
from itertools import zip_longest

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_cons.txt'))
# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_cons_test.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
print(raw)
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    # strand = raw[x][13:]
    strand = raw[x][13:]
    fatsas.append(strand)
print(f"Strands: {fatsas}")

for i, fatsa in enumerate(fatsas):
    print(f"{i}: " + fatsa)

# Create matrix profiles
profiles = []
length = len(fatsas[1])
for x in range(0, length):
    countA, countC, countG, countT = (0,)*4
    for y in range(0, len(fatsas)):
        if fatsas[y][x] == "A":
            countA += 1
        elif fatsas[y][x] == "C":
            countC += 1
        elif fatsas[y][x] == "G":
            countG += 1
        elif fatsas[y][x] == "T":
            countT += 1
    profiles.append([countA, countC, countG, countT])
print(profiles)

# Find optimal strand
solution = ""
for profile in profiles:
    max_value = max(profile)
    max_index = profile.index(max_value)
    if max_index == 0:
        solution += "A"
    elif max_index == 1:
        solution += "C"
    elif max_index == 2:
        solution += "G"
    elif max_index == 3:
        solution += "T"
print(solution)

# Format reverse profiles array
letters = []
for x in range(0, 4):
    letter = []
    for y in range(0, len(solution)):
        letter.append(profiles[y][x])
    letters.append(letter)
for i, c in enumerate('ACGT'):
    print(f"{c}: " + " ".join( str(x) for x in letters[i] ))
