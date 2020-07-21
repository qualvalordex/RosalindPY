#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/fib/

def rabbit_population(num_months, num_offspring):
    if num_months < 3:
        return 1

    return rabbit_population(num_months-1, num_offspring) + num_offspring * rabbit_population(num_months-2, num_offspring)

print(rabbit_population(35,2))
#LOGS 11453246123