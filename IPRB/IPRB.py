import os
import sys
import random

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_fib.txt'))
# vars = file.read()
vars = "2 2 2"
k = int(vars.split(' ')[0]) # YY homozygous dominant
m = int(vars.split(' ')[1]) # Yy heterozygous
n = int(vars.split(' ')[2]) # yy homozygous recessive
total = k + m + n

# Get random parents
rand1 = random.randint(0,2)
rand2 = random.randint(0,2)

# Combinations
def mendel_pair(gene1, gene2):
    child = 0
    if gene1 == 0 and gene2 == 0:   # YY - YY
        child = 100
    elif gene1 == 0 and gene2 == 1: # YY - Yy
        child = 100
    elif gene1 == 0 and gene2 == 2: # YY - yy
        child = 100
    elif gene1 == 1 and gene2 == 0: # Yy - YY
        child = 100
    elif gene1 == 1 and gene2 == 1: # Yy - Yy
        child =  75
    elif gene1 == 1 and gene2 == 2: # Yy - yy
        child =  50
    elif gene1 == 1 and gene2 == 0: # yy - YY
        child = 100
    elif gene1 == 1 and gene2 == 1: # yy - Yy
        child =  50
    elif gene1 == 1 and gene2 == 2: # yy - yy
        child =   0
    return child

stats = mendel_pair(rand1, rand2)
print(stats)
