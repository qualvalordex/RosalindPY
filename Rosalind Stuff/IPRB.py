#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/iprb/

from scipy.special import comb

def dominant_probability(dominant, heterozygous, recessive):
    total_population = dominant + heterozygous + recessive
    total_offspring = 4 * comb(total_population, 2)
    total_dominant = 4 * comb(dominant, 2) + 4 * dominant * heterozygous + 4 * dominant * recessive + 3 * comb(heterozygous, 2) + 2 * heterozygous * recessive

    prob_dominant = total_dominant / total_offspring
    print(prob_dominant)

    return prob_dominant

dominant_probability(15,24,28)
#LOGS 0.6458616010854816