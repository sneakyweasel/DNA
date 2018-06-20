import os
import sys
import bisect

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_inv.txt'))
lines = [line.rstrip('\n') for line in file]

n = lines[0]
arr = [int(x) for x in lines[1].split(" ")]

def merge_list(left,right):
    result = list()
    i,j = 0, 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result, inv_count

def sort_and_count(array):
    if len(array) < 2:
        return array, 0
    middle = int(len(array) / 2)
    left,inv_left = sort_and_count(array[:middle])
    right,inv_right = sort_and_count(array[middle:])
    merged, count = merge_list(left,right)
    count += (inv_left + inv_right)
    return merged, count

print(sort_and_count(arr)[1])
