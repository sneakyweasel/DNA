import os
import sys
import bisect

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_mer.txt'))
lines = [line.rstrip('\n') for line in file]

n1 = lines[0]
arr1 = [int(x) for x in lines[1].split(" ")]
n2 = lines[2]
arr2 = [int(x) for x in lines[3].split(" ")]

sarr = [str(x) for x in sorted(arr1 + arr2)]
print(" ".join(sarr))
