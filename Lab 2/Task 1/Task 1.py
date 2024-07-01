import math
import random
def overlap_penalty(time_slots,N,T):
    cheack_arr=[]
    overlap_P=0
    for i in range(T):
        indivisual_slot=time_slots[i*N:(i+1)*N]
        # print(indivisual_slot)
        count=max(indivisual_slot.count("1")-1,0)
        overlap_P+=count
    return overlap_P
def consistency_panelty(time_slots,N,T):
    panelty=0

    for i in range(N):
        panelty_count = 0
        for j in range(T):
            panelty_count+=int(time_slots[j*N+i])
            # print(panelty_count)
            # panelty-=1

        panelty+=abs(panelty_count-1)
        # print(panelty)
    return panelty

def calculate_fitness(time_slots,N,T):
    panelty= -(overlap_penalty(time_slots,N,T)+consistency_panelty(time_slots,N,T))
    return panelty
def create_population(n,t,population_size):
    population_list=[]

    for j in range(population_size):
        population = ""
        for i in range(n*t):
            population+=random.choice('01')
        # print(population)
        population_list.append(population)
    return population_list
def parents_selection(population):
    return random.choice(population),random.choice(population)
def crossover(parent1,parent2,N,T):
    point=random.randint(0,N*T-1)
    child1=parent1[0:point]+parent2[point:]
    child2=parent2[0:point]+parent1[point:]
    return child1,child2
def mutation(child,N,T):
    point=random.randint(1,N*T-1)
    list1=list(child)
    # print(list1)
    if list1[point]=="1":
        list1[point]="0"
    return "".join(list1)

def genetic_algo(N,T,population_size,iterations):
    population=create_population(N,T,population_size)
    # print(population)
    lowest_fitness=-math.inf
    best_slot=None
    for _ in range(iterations):
        new_population=[]
        for _ in range(population_size//2):
            parent1,parent2=parents_selection(population)
            child1,child2=crossover(parent1,parent2,N,T)
            new_population.extend([mutation(child1,N,T),mutation(child2,N,T)])
        population=new_population
        for slots in population:
            fitess_value=calculate_fitness(slots,N,T)

            if fitess_value>lowest_fitness:
                lowest_fitness = fitess_value
                best_slot = slots

            if lowest_fitness==0:
                break
    return lowest_fitness,best_slot


N,T=int(input("Enter N: ")),int(input("Enter T:"))
courses=[input("Enter courses: ") for i in range(N)]
if T<N:
    print("T can't be less than N")
else:
    fitness,schedule=genetic_algo(N,T,population_size=100,iterations=1000)
    print(schedule)
    print(fitness)