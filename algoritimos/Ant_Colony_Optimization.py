# ==================================================
# 2) ACO - Ant Colony Optimization (Ant System/ACS)
# ==================================================
import random
from typing import List, Tuple
from problema.utils import *
def solve_aco(problem: TSPProblem, n_ants=30, iterations=300,
              alpha=1.0, beta=5.0, rho=0.5, q=100.0, seed=42,
              use_two_opt=True):
    random.seed(seed)
    n = problem.n
    # feromônio inicial
    tau0 = 1.0
    tau = [[tau0 for _ in range(n)] for _ in range(n)]
    eta = [[0.0]*n for _ in range(n)]  # heurística = 1/d
    for i in range(n):
        for j in range(n):
            if i != j and problem.dist[i][j] > 0:
                eta[i][j] = 1.0 / problem.dist[i][j]

    best_tour = None
    best_len = float('inf')

    for it in range(iterations):
        all_tours = []
        all_lengths = []

        for _ in range(n_ants):
            # constrói passeio
            start = random.randrange(n)
            unvisited = set(range(n))
            unvisited.remove(start)
            tour = [start]
            current = start

            while unvisited:
                probs = []
                denom = 0.0
                for j in unvisited:
                    val = (tau[current][j] ** alpha) * (eta[current][j] ** beta)
                    probs.append((j, val))
                    denom += val
                # escolha
                r = random.random()
                acc = 0.0
                chosen = None
                for j, val in probs:
                    p = val / denom if denom > 0 else 1.0 / len(probs)
                    acc += p
                    if r <= acc:
                        chosen = j
                        break
                if chosen is None:
                    chosen = random.choice(list(unvisited))
                tour.append(chosen)
                unvisited.remove(chosen)
                current = chosen

            L = problem.length(tour)
            all_tours.append(tour)
            all_lengths.append(L)

            if L < best_len:
                best_tour, best_len = tour[:], L

        # evaporação
        for i in range(n):
            for j in range(n):
                tau[i][j] *= (1 - rho)
                if tau[i][j] < 1e-12:
                    tau[i][j] = 1e-12

        # depósito de feromônio (opção: só melhor da iteração)
        best_idx = min(range(len(all_lengths)), key=lambda k: all_lengths[k])
        tour = all_tours[best_idx]
        L = all_lengths[best_idx]
        deposit = q / L

        for i in range(n):
            a = tour[i]
            b = tour[(i+1) % n]
            tau[a][b] += deposit
            tau[b][a] += deposit

    if use_two_opt and best_tour is not None:
        best_tour = two_opt(best_tour, problem)
        best_len = problem.length(best_tour)

    return best_tour, best_len
