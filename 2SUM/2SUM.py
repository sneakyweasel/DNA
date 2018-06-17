import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_2sum.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
k = int(first_line.split(" ")[0])
n = int(first_line.split(" ")[1])

# Process inputs
inputs = []
for line in lines:
    inputs.append([int(x) for x in line.split(" ")])
print(f"LEN: {len(inputs)}")

# Brute
for input in inputs:
    solution = []
    for x in range(0, n):
        for y in range(x+1, n):
            if input[x] == -input[y]:
                solution.append([x+1, y+1])

    if len(solution) > 1:
        print(" ".join(str(y) for y in solution[-1]))
    elif len(solution) == 1:
        print(" ".join(str(y) for y in solution[-1]))
    else:
        print("-1")
