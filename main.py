from algoritimos.Ant_Colony_Optimization import solve_aco
from algoritimos.Algoritmo_Genético import solve_ga
from algoritimos.Grey_Wolf_Optimizer import solve_gwo
from problema.utils import TSPProblem
# ==================================================
# Exemplo de uso
# ==================================================

if __name__ == "__main__":
    # Exemplo simples com 15 cidades (coordenadas em um plano)
    coords = [
        (0,0),(1,5),(5,2),(6,6),(8,3),
        (2,7),(7,8),(3,3),(4,7),(9,5),
        (6,1),(2,2),(8,8),(1,9),(9,1)
    ]
    tsp = TSPProblem(coords)

    print("=== GA ===")
    ga_tour, ga_len = solve_ga(tsp, pop_size=200, generations=800, seed=1)
    print("distância:", round(ga_len, 3))
    print("rota:", ga_tour)

    print("\n=== ACO ===")
    aco_tour, aco_len = solve_aco(tsp, n_ants=40, iterations=400, seed=1)
    print("distância:", round(aco_len, 3))
    print("rota:", aco_tour)

    print("\n=== GWO (Random Keys) ===")
    gwo_tour, gwo_len = solve_gwo(tsp, n_wolves=50, iterations=800, seed=1)
    print("distância:", round(gwo_len, 3))
    print("rota:", gwo_tour)
