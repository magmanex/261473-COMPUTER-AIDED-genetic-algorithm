# TITLE : COMPUTER-AIDED MANUFACTURING
# COURSE NO : 261473
# Developed By(github) : magmanex
# Name : Arinchai Nanjaruwong
# STUID : 580610692
import random

GA_POPSIZE = 2048 #Population size
GA_MAXITER = 1648 #Maximum iterations
GA_ELITERATE = 0.10 # Elitism rate
GA_MUTPERC = 0.25 # Mutation rate
PRINT_INTER = 0 # Print status every this iterations/generations

GA_ELITSIZE = (GA_POPSIZE * GA_ELITERATE) # Number of elites 
GA_MUTCHANCE = 4

TARGET_LEN =  20 # The length of int target (below)
CHROMOSOME_MAX = 10 # The maximum size of a chromosome

target = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

class ga_memb:
    sol = []
    fitness = 0

def init_pop(pop):
    zero_fitness(pop)

def zero_fitness(pop):
    for i in range(GA_POPSIZE):
        pop[i].fitness = 0

def randall_sols(pop):
    for i in range(GA_POPSIZE):
        for j in range(TARGET_LEN):
            pop[i].sol[j] = random.randint(0,CHROMOSOME_MAX)

# For every correct chromosome, we add 1 to the score
# Thus, a perfect score is equal to TARGET_LEN

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

def mutate(pop):
    for i in GA_ELITERATE:
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
