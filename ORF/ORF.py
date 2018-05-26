import os
import sys
import string
import itertools

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_orf.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
print(raw)
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    strand = raw[x][13:]
    fatsas.append(strand)
print(f"Strands: {fatsas}")

def convert_to_rna(dna):
    return dna.replace("T", "U")

def convert_rna_to_protein(rna):
    # Convert codon file to array
    codons = []
    file = open(os.path.join(os.path.dirname(sys.argv[0]), 'codon.txt'))
    for line in file.read().splitlines():
        triplet = line.split(" ")[0]
        letter  = line.split(" ")[1]
        codons.append([triplet, letter])
    # Chunk rna into triplets
    chunks = (rna[pos:pos + 3] for pos in range(0, len(rna), 3))
    triplets = []
    for chunk in chunks:
        triplets.append(''.join(chunk))
    # Translate triplets into proteins
    solution = []
    for triplet in triplets:
        for codon in codons:
            if triplet == codon[0]:
                solution.append(codon[1])
    return ''.join(solution)

def start_codon(rna):
    start = "AUG"
    return [rna.index(start)]

def end_codon(rna):
    pos = []
    end_codons = ["UAA", "UAG", "UGA"]
    for end_codon in end_codons:
        pos.append(rna.index(end_codon))
    return pos

# Main
main = fatsas[0]
rna = convert_to_rna(main)
starts = start_codon(rna)
ends = end_codon(rna)

# Combination of starts and ends
combinations = list(itertools.product(starts, ends))
for combination in combinations:
    orf_rna = rna[combination[0]+3:combination[1]:]
    orf_protein = convert_rna_to_protein(orf_rna)
    print(f"{combination}")
    print(orf_rna)
    print(orf_protein)

# protein = convert_rna_to_protein(rna)
# print(f"RNA   {len(main)}: {rna}")
# print(f"Starts: {starts}")
# print(f"Ends  : {ends}")
# print(f"Combi : {combinations}")
