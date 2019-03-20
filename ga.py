# TITLE : COMPUTER-AIDED MANUFACTURING
# COURSE NO : 261473
# Developed By(github) : magmanex
# Name : Arinchai Nanjaruwong
# STUID : 580610692
import random

#Population size
GA_POPSIZE = 2048 
#Maximum iterations
GA_MAXITER = 1648 
#Elitism rate
GA_ELITERATE = 0.10 
#Mutation rate
GA_MUTPERC = 0.25 
#Print status every this iterations/generations
PRINT_INTER = 0 

GA_ELITSIZE = (GA_POPSIZE * GA_ELITERATE) #Number of elites 
GA_MUTCHANCE = 4

TARGET_LEN =  20 #The length of int target (below)
CHROMOSOME_MAX = 10 #The maximum size of a chromosome

target = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

class Ga_memb:
    sol = []
    fitness = 0

def main():
    i = 0
    j = 0

    print("Test")

    #Create our two populations
    #They are really the same population, but we havae two for speed
    pop_a = Ga_memb()
    pop_b = Ga_memb()
    
    init_pop(pop_a)
    init_pop(pop_b)

    pop = pop_a
    buf = pop_b

    while i < GA_MAXITER :
        calc_fitness(pop)
        insertion_sort_ga_memb(pop,GA_POPSIZE)

        #Print our stats every PRINT_INTER iterations of the loop
        if j > PRINT_INTER :
            print_best(pop,i)
            j = 0
        
        #If the number of correct parts is the same as the TARGET_LEN, it is all correct :)
        if pop[GA_POPSIZE - 1].fitness == TARGET_LEN :
            break

        mate_pop(pop , buf)
        swap_pts(pop , buf)

        i += 1
        j += 1

    print_best(pop,i)

if __name__== "__main__":
  main()

def init_pop(pop):
    zero_fitness(pop)
    randall_sols(pop)

def zero_fitness(pop):
    for i in range(GA_POPSIZE):
        pop[i].fitness = 0

def randall_sols(pop):
    for i in range(GA_POPSIZE):
        for j in range(TARGET_LEN):
            pop[i].sol[j] = random.randint(0,CHROMOSOME_MAX)

#For every correct chromosome, we add 1 to the score
#Thus, a perfect score is equal to TARGET_LEN

def calc_fitness(pop):
    fitness = 0
    for i in range(GA_POPSIZE):
        fitness = 0
        for j in range(TARGET_LEN):
            if pop[i].sol[j] == target[j]:
                fitness+=1
        pop[i].fitness = fitness

def insertion_sort_ga_memb(a , asize):
    d = []

    k = asize
    for i in range(k):
        d = a[i]
        j = i - 1
        while j >= 0 and a[j].fitness > d.fitness :
            a[j + 1] = a[j]
            j = j - 1

def print_best(pop , gen):
    i = 1
    print("At gen" , gen , "best: " , pop[GA_POPSIZE - 1].sol)
    for i in range(TARGET_LEN):
        print("," , pop[GA_POPSIZE - 1].sol + i)
    print("(" , (pop[GA_POPSIZE - 1].fitness * 100 ) / TARGET_LEN , ")" )

def mate_pop(pop , buf):
    i = GA_ELITSIZE
    j = 0
    randint = 0

    #Copy over the elites
    cp_mems(pop , buf , GA_ELITSIZE)

    #Don't touch the elites, mate the others
    while i < GA_POPSIZE :
        randint = random.random() % TARGET_LEN
        j = 0
        #The first half of the chromosomes don't change
        while j < randint :
            buf[i].sol[j] = pop[i].sol[j]
            buf[i+1].sol[j] = pop[i].sol[j]
            j += 1
        j = randint
        while j < TARGET_LEN :
            buf[i].sol[j] = pop[i+1].sol[j]
            buf[i+1].sol[j] = pop[i].sol[j]
            j += 1
        i += 2
    mutate(buf)

#Swap pt1 and pt2
def swap_pts(pt1 , pt2):
    pt_tmp = pt2
    pt2 = pt1
    pt1 = pt_tmp

#Mutates some of the population
def mutate(pop):
    for i in range(GA_ELITERATE):
        if random.random() % GA_MUTCHANCE == 0:
            randint = random.random()
            pop[0].sol[randint % TARGET_LEN] = randint

def cp_mems(src , targ , size):
    i = GA_POPSIZE - 1
    while i >= size:
        targ[i].fitness = src[i].fitness
        j = 0
        while j < TARGET_LEN:
            targ[i].sol[j] = src[i].sol[j]
            j += 1
        i += 1
