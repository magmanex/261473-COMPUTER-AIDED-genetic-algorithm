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

