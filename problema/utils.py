import math
from typing import List, Tuple
# =========================
# Utilidades do problema
# =========================

class TSPProblem:
    def __init__(self, coords: List[Tuple[float, float]]):
        self.coords = coords
        self.n = len(coords)
        self.dist = [[0.0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            xi, yi = coords[i]
            for j in range(self.n):
                xj, yj = coords[j]
                self.dist[i][j] = math.hypot(xi - xj, yi - yj)

    def length(self, tour: List[int]) -> float:
        total = 0.0
        for i in range(self.n):
            a = tour[i]
            b = tour[(i+1) % self.n]
            total += self.dist[a][b]
        return total
    
def two_opt(tour: List[int], problem: TSPProblem) -> List[int]:
    """Pequena melhoria local 2-opt (até não melhorar mais)."""
    best = tour[:]
    best_len = problem.length(best)
    improved = True
    while improved:
        improved = False
        for i in range(1, problem.n - 2):
            for j in range(i + 1, problem.n):
                if j - i == 1:
                    continue
                new = best[:]
                new[i:j] = reversed(new[i:j])
                new_len = problem.length(new)
                if new_len + 1e-12 < best_len:
                    best, best_len = new, new_len
                    improved = True
        # sai se não houver melhora
    return best
