#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/gc/

from utils.read_fasta import read_fasta
from DNA import count_nucleotids

def gc_content(dna_sequence):
    A, C, G, T = count_nucleotids(dna_sequence)
    return ((C+G)/len(dna_sequence))*100

def max_gc_content(file_name):
    sequences = read_fasta(file_name)
    gc_dict = {}
    for sequence in sequences.keys():
        gc_dict[sequence] = gc_content(sequences[sequence])
    
    max_key = max(gc_dict, key=gc_dict.get)
    
    return max_key, gc_dict[max_key]

print(max_gc_content('data/GC_challenge.fasta'))
#LOGS Rosalind_7573 55.30474040632054