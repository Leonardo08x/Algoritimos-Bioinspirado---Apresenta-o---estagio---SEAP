import random
from typing import List, Tuple
from problema.utils import *
# ==================================================
# 3) Grey Wolf Optimizer (GWO) com Random Keys
# ==================================================

def decode_random_keys(keys: List[float]) -> List[int]:
    """Transforma vetor contínuo [0,1]^n em permutação via ordenação."""
    return [i for i, _ in sorted(enumerate(keys), key=lambda kv: kv[1])]

def clamp01(x: float) -> float:
    return 0.0 if x < 0.0 else (1.0 if x > 1.0 else x)

def solve_gwo(problem: TSPProblem, n_wolves=40, iterations=600, seed=42,
              use_two_opt=True):
    random.seed(seed)
    n = problem.n

    # inicializa chaves aleatórias em [0,1]
    wolves = [[random.random() for _ in range(n)] for _ in range(n_wolves)]

    def fitness(keys):
        tour = decode_random_keys(keys)
        return problem.length(tour)

    # avalia
    fitnesses = [fitness(w) for w in wolves]
    # identifica alpha, beta, delta
    def update_abc():
        idx = sorted(range(n_wolves), key=lambda i: fitnesses[i])[:3]
        return idx[0], idx[1], idx[2]

    alpha, beta, delta = update_abc()

    for t in range(iterations):
        a = 2 - 2 * (t / (iterations - 1))  # decresce de 2 para 0
        for i in range(n_wolves):
            if i in (alpha, beta, delta):
                continue
            new_pos = []
            for d in range(n):
                r1, r2 = random.random(), random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * wolves[alpha][d] - wolves[i][d])
                X1 = wolves[alpha][d] - A1 * D_alpha

                r1, r2 = random.random(), random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * wolves[beta][d] - wolves[i][d])
                X2 = wolves[beta][d] - A2 * D_beta

                r1, r2 = random.random(), random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * wolves[delta][d] - wolves[i][d])
                X3 = wolves[delta][d] - A3 * D_delta

                x = (X1 + X2 + X3) / 3.0
                new_pos.append(clamp01(x))
            wolves[i] = new_pos

        # reavaliar
        fitnesses = [fitness(w) for w in wolves]
        alpha, beta, delta = update_abc()

    best_keys = wolves[alpha]
    best_tour = decode_random_keys(best_keys)
    if use_two_opt:
        best_tour = two_opt(best_tour, problem)
    best_len = problem.length(best_tour)
    return best_tour, best_len
