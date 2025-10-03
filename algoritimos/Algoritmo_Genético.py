# ==================================================
# 1) Algoritmo Genético (GA) para TSP (permutações)
# ==================================================
import random
from typing import List, Tuple
from problema.utils import *
from problema.static_graph_generator import static_graph, gif_maker
def ox_crossover(p1: List[int], p2: List[int]) -> List[int]:
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n
    child[a:b+1] = p1[a:b+1]
    fill = [gene for gene in p2 if gene not in child]
    idx = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child

def mutate_swap(chrom: List[int], rate: float) -> None:
    n = len(chrom)
    for _ in range(n):
        if random.random() < rate:
            i, j = random.sample(range(n), 2)
            chrom[i], chrom[j] = chrom[j], chrom[i]

def tournament(pop, fitnesses, k=3):
    best = None
    best_fit = float('inf')
    for _ in range(k):
        i = random.randrange(len(pop))
        if fitnesses[i] < best_fit:
            best = pop[i]
            best_fit = fitnesses[i]
    return best[:]

def solve_ga(coords, problem: TSPProblem , pop_size=150, generations=800,
             cx_rate=0.9, mut_rate=0.02, elitism=2, seed=42,
             use_two_opt=True):
    random.seed(seed)
    n = problem.n
    base = list(range(n))

    # população inicial: permutações aleatórias
    population = []
    for _ in range(pop_size):
        p = base[:]
        random.shuffle(p)
        population.append(p)
    def evaluate(pop):
        return [problem.length(ind) for ind in pop]

    fitnesses = evaluate(population)
    best = population[min(range(pop_size), key=lambda i: fitnesses[i])][:]
    best_len = min(fitnesses)

    for g in range(generations):
        # elitismo
        elites_idx = sorted(range(pop_size), key=lambda i: fitnesses[i])[:elitism]
        new_pop = [population[i][:] for i in elites_idx]

        # reprodução
        while len(new_pop) < pop_size:
            p1 = tournament(population, fitnesses)
            p2 = tournament(population, fitnesses)
            child = ox_crossover(p1, p2) if random.random() < cx_rate else p1[:]
            mutate_swap(child, mut_rate)
            new_pop.append(child)

        population = new_pop
        fitnesses = evaluate(population)

        # atualiza melhor
        idx = min(range(pop_size), key=lambda i: fitnesses[i])
        if fitnesses[idx] < best_len:
            best, best_len = population[idx][:], fitnesses[idx]
            static_graph(best_len, best, g, coords)

    if use_two_opt:
        best = two_opt(best, problem)
        best_len = problem.length(best)
        gif_maker()
    return best, best_len
