import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_3sum.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
k = int(first_line.split(" ")[0])
n = int(first_line.split(" ")[1])
print(f"K: {k} - N: {n}")

# Process inputs
inputs = []
for line in lines:
    inputs.append([int(x) for x in line.split(" ")])
print(f"LEN: {len(inputs)}")

# 3SUM fast algorithm
def threeSum(nums):
    nums = list(nums)
    n = len(nums)
    sol = []
    for i in range(0, n-2):
        a = nums[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = nums[start]
            c = nums[end]
            if (a + b + c) == 0:
                sol = [a, b, c]
                start = end
            elif (a + b + c) > 0:
                end -= 1
            else:
                start += 1
    if len(sol) > 0:
        return sol
    else:
        return [-1]

# Indices reprocess
solution = []
for input in inputs:
    arrays = []
    result = threeSum(input)
    print(result)
    if len(result) == 1:
        solution.append([-1])
    else:
        index_array = []
        p = result[0]
        q = result[1]
        r = result[2]
        # print(f"SUM: {p} + {q} + {r} = {p + q + r}")
        for num in result:
            index_array.append(input.index(num) + 1)
        solution.append(sorted(index_array))


for z in solution:
    print(" ".join(str(y) for y in z))
