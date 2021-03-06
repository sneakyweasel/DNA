import os
import sys
import random
import itertools
from scipy.special import comb

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lia.txt'))
vars = file.read()
k = int(vars.split(' ')[0]) # number of generations
N = int(vars.split(' ')[1]) # number of Aa Bb organisms

# [Aa Bb] + [Aa Bb]
# AA (1) - homo dom
# Aa (2) - hetero
# aa (1) - homo rec

# GEN 0:
# start = [Aa, Bb]

# GEN 1:
# Prob(Aa Bb) = Prob(Aa) * Prob(Bb)
# Prob(Aa Bb) = 2/4 * 2/4 = 1/4
# Prob(Aa Bb) = 2/4 * 2/4 = 1/4
# Total: 2

# GEN 2:
# Prob(Aa Bb) = Prob(Aa) * Prob(Bb)
# Prob(Aa Bb) = 2/4 * 2/4
# Total: 2

def firstLaw():
    total = AA + Aa + aa
    totalComb = comb(total, 2)
    dominant = comb(AA, 2)              \
                + AA * Aa               \
                + AA * aa               \
                + .5 * Aa * aa          \
                + .75 * comb(Aa, 2)
    prob_dom = dominant / totalComb
    return prob_dom
