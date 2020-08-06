def read_fasta(file_name):
    with open(file_name, 'r') as fasta:
        fasta_list = ''.join(fasta).strip().split('\n')
        #del fasta_list[-1]
    return fasta_list

def get_sequences(fasta_list):
    sequences = []
    for element in fasta_list:
        if not element.startswith('>'):
            sequences.append(element)
    #print(sequences)
    return sequences

def get_labels(fasta_list):
    labels = []
    for element in fasta_list:
        if element.startswith('>'):
            labels.append(element.replace('>','').replace('\n',''))
    #print(labels)
    return labels

def dict_from_fasta(file_name):
    fasta_dict = {}
    fasta_list = read_fasta(file_name)
    sequences = get_sequences(fasta_list)
    labels = get_labels(fasta_list)
    if len(sequences) == len(labels):
        size = len(sequences)
        for i in range(0,size):
            fasta_dict[labels[i]] = sequences[i]
    return fasta_dict