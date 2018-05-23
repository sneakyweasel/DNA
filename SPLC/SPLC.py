import os
import sys

# Read and process FASTA
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_splc.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
print(f"Raw: {raw}")
strands = []
for x in range(1, len(raw), 1):
    strand = raw[x][13:]
    strands.append(strand)
main = strands.pop(0)
print(f"Strands: {strands}")


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
                if codon[1] == "Stop":
                    break
                else:
                    solution.append(codon[1])
    return ''.join(solution)

# Order introns by size
sorted_introns = sorted(strands, key=len)[::-1]
print(f"Introns: {sorted_introns}")

# Remove introns
print(f"Main  {len(main)}: {main}")
for intron in sorted_introns:
    main = main.replace(intron, "")

# Main
rna = convert_to_rna(main)
protein = convert_rna_to_protein(rna)
print(f"Exons {len(main)}: {main}")
print(f"RNA   {len(main)}: {rna}")
print(f"{protein}")
