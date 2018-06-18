import os
import sys
import heapq_max

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_hs.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(f"N: {n}")

# Process inputs
nums = [int(x) for x in lines[0].split(" ")]
# print(f"NUMS: {nums}")

# heapsort
def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

  # in pseudo-code, heapify only called once, so inline it here
  for start in range(int((len(lst)-2)/2), -1, -1):
    siftdown(lst, start, len(lst)-1)

  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst

def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

result = heapsort(nums)
print(" ".join([str(x) for x in result]))
