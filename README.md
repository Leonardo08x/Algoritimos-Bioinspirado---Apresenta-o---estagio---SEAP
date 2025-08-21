# TSP Bioinspirado: GA, ACO e GWO

**Autor:** Leonardo Cunha da Rocha

Este repositório contém implementações em Python de três **algoritmos bioinspirados** para resolver o **Problema do Caixeiro Viajante (TSP)**:

1. **Algoritmo Genético (GA)**
2. **Colônia de Formigas (Ant Colony Optimization, ACO)**
3. **Otimização por Lobo Cinzento (Grey Wolf Optimizer, GWO)**

O objetivo é **complementar minha apresentação sobre algoritmos bioinspirados**, permitindo que colegas de trabalho testem, experimentem e visualizem os algoritmos em ação.

---

## Estrutura do Projeto

```
meu_projeto/
├── algoritimos/
│   ├── __init__.py
│   ├── ant_colony_optimization.py
│   ├── algoritmo_genetico.py
│   └── grey_wolf_optimizer.py
├── problema
|   ├── utils.py
├── main.py
└── README.txt
```

- `algoritimos/` – Pasta contendo os três algoritmos implementados separadamente.  
- `main.py` – Exemplo de uso, mostrando como importar e rodar cada algoritmo.  
- `README.txt` – Documentação do projeto.

---

## Como usar

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/tsp-bioinspirado.git
cd tsp-bioinspirado
```

### 2. Instalar dependências
O código usa apenas **Python padrão**, sem bibliotecas externas.  
Recomendado: Python 3.8 ou superior.

### 3. Rodar o exemplo
```bash
python main.py
```

Isso irá executar os três algoritmos em um conjunto de cidades de exemplo, mostrando:

- Rota encontrada  
- Distância total

### 4. Importar em outros scripts
```python
from algoritimos.Ant_Colony_Optimization import solve_aco
from algoritimos.Algoritmo_Genético import solve_ga
from algoritimos.Grey_Wolf_Optimizer import solve_gwo
```

E então você pode chamar as funções com seu próprio conjunto de cidades (`TSPProblem`).

---

## Algoritmos implementados

- **GA (Algoritmo Genético):**  
  - População de permutações  
  - Crossover por ordem (OX)  
  - Mutação por troca  
  - Seleção por torneio e elitismo  

- **ACO (Colônia de Formigas):**  
  - Feromônio + heurística (1/distância)  
  - Evaporação e reforço pelo melhor tour  
  - Escolha probabilística das próximas cidades  

- **GWO (Otimização por Lobo Cinzento):**  
  - Adaptado para TSP usando **Random Keys**  
  - Equações clássicas de ataque e caça de lobos  
  - Converte vetor contínuo em permutação  

- **Extra:** Todas as soluções podem ser refinadas usando **2-opt**, uma melhoria local simples.

---

## Créditos

- Leonardo Cunha da Rocha – implementação, organização e documentação do projeto.  
- Inspiração nos conceitos de **algoritmos bioinspirados** aplicados a problemas combinatórios.

---


Este projeto é **open-source** e livre para estudo e uso interno em empresas ou instituições.  
Pode ser modificado e compartilhado, desde que seja mantido o crédito ao autor.
