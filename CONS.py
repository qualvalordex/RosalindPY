#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/cons/

from utils.fasta_reader import dict_from_fasta
import numpy as np

fl = dict_from_fasta('./data/rosalind_cons.fasta')
#print(fl)
sequence_len = len(list(fl.values())[0])
sequence_matrix = list(fl.values())
profile = np.zeros((4, sequence_len), dtype=int)

for j in range(0,sequence_len):
    for i in range(0, len(fl.values())):
        if sequence_matrix[i][j] == 'A':
            profile[0][j] += 1
        if sequence_matrix[i][j] == 'C':
            profile[1][j] += 1
        if sequence_matrix[i][j] == 'G':
            profile[2][j] += 1
        if sequence_matrix[i][j] == 'T':
            profile[3][j] += 1

max_line = 0
max_value = 0
cons_string = ''

for j in range(0,len(profile[0])):
    max_line = 0
    max_value = 0
    for i in range(0,4):
        if max_value < profile[i][j]:
            max_value = profile[i][j]
            max_line = i
    #print(max_line)
    if max_line == 0:
        cons_string = cons_string + 'A'
    if max_line == 1:
        cons_string = cons_string + 'C'
    if max_line == 2:
        cons_string = cons_string + 'G'
    if max_line == 3:
        cons_string = cons_string + 'T'

txt = cons_string
nucl = ['A', 'C', 'G', 'T']
for n in range(0,4):
    txt = txt + '\n' + nucl[n] + ': '
    for i in profile[n]:
        txt = txt + str(i) + ' '

with open('./data/cons_result.txt', 'w') as out:
    out.write(txt)

print(txt)
#print('A: ', profile[0])
#print('C: ', profile[1])
#print('G: ', profile[2])
#print('T: ', profile[3])