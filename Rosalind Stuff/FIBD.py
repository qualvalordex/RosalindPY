#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/fibd/

#The main idea is to sum all generation population

def mortal_rabbits(num_months, lifespan):
    generation = [0]*lifespan
    temp = []

    #Considering starts at n = 2
    generation[0] = 0
    generation[1] = 1

    for i in range(2, num_months):
        temp = list(generation)
        generation[0] = sum(generation[1:])
        for k in range(1, lifespan):
            generation[k] = temp[k-1]
    
    return sum(generation)

print(mortal_rabbits(85,17))
#LOGS 257431373055877146