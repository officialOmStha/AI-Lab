import math
import random

# Example graph (neighbors)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic (lower is better, goal = F → 0)
h = {
    'A': 7,
    'B': 5,
    'C': 3,
    'D': 6,
    'E': 2,
    'F': 0
}

def simulated_annealing(graph, start, goal, h):
    current = start
    T = 100.0          # initial temperature
    cooling = 0.90     # cooling rate

    path = [current]

    while T > 1:
        if current == goal:
            break

        neighbors = graph[current]
        if not neighbors:
            break

        # pick random neighbor
        next_node = random.choice(neighbors)

        # difference in heuristic
        delta = h[next_node] - h[current]

        # accept if better OR with probability if worse
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = next_node
            path.append(current)

        # cool down
        T *= cooling

    return path, current


# RUN
path, final_node = simulated_annealing(graph, 'A', 'F', h)

print("Path taken:", path)
print("Final node:", final_node)