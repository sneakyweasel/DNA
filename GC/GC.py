import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_gc.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
# blob = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
sequences = blob.split('>')
sequences.pop(0)
fasta = []

def gc_content( dna ):
    countC = dna.count('C')
    countG = dna.count('G')
    gc = ((countC + countG) / len(dna) * 100)
    return gc

def getKey(item):
    return -item[1]

for seq in sequences:
    name = seq[0:13]
    dna  = seq[13:]
    gc   = gc_content(dna)
    fasta.append([name, gc])

# Sort results by GC
result = sorted(fasta, key=getKey)

print(result[0][0])
print(result[0][1])
