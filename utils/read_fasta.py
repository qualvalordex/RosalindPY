#Function to return a dict from FASTA data

def read_fasta(file_name):
    with open (file_name, 'r') as fasta:
        lines = [line.strip() for line in fasta]
        labels = []
        sequences = []
        fasta_dict = {}
        for line in lines:
            if line.startswith('>'):
                labels.append(line)
            else:
                sequences.append(line)
        
        if len(labels) == len(sequences):
            for index in range(len(labels)):
                fasta_dict[labels[index].replace('>','')] = sequences[index]
            return fasta_dict
        else:
            print('Error: labels and sequences do not have same length.')