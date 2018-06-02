import os
import sys
import random
import itertools
from scipy.special import comb

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_iprb.txt'))
vars = file.read()
# vars = "2 2 2"
AA = int(vars.split(' ')[0]) # YY homozygous dominant
Aa = int(vars.split(' ')[1]) # Yy heterozygous
aa = int(vars.split(' ')[2]) # yy homozygous recessive

# Chance of dominant trait (maj) from parents
def punnett_pair(gene1, gene2):
    child = 0
    if   gene1 == 0 and gene2 == 0: # YY - YY
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
    elif gene1 == 2 and gene2 == 0: # yy - YY
        child = 100
    elif gene1 == 2 and gene2 == 1: # yy - Yy
        child =  50
    elif gene1 == 2 and gene2 == 2: # yy - yy
        child =   0
    return child / 100

# total population
total = AA + Aa + aa

# total combinations
totalComb = comb(total, 2)

# dominant population
dominant = comb(AA, 2)              \
            + AA * Aa               \
            + AA * aa               \
            + .5 * Aa * aa          \
            + .75 * comb(Aa, 2)

# probability for dominant trait
prob_dom = dominant / totalComb
print(prob_dom)
