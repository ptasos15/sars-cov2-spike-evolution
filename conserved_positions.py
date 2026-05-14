from Bio import AlignIO
import sys

alignment = AlignIO.read(sys.argv[1], "fasta")
length = alignment.get_alignment_length()
nseq = len(alignment)

for i in range(length):
    column = alignment[:, i]
    residues = [aa for aa in column if aa not in ["-", "X"]]
    
    if len(residues) == 0:
        continue
    
    if len(set(residues)) == 1:
        print(i+1, residues[0])

