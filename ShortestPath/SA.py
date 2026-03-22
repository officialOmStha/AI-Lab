import math
import random

# Simulated Annealing Algorithm

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces (or leave blank if none): ").strip()
    neighbors = neighbors_input.split() if neighbors_input else []
    graph[node] = neighbors

# Input heuristic values for each node
h = {}
print("\nEnter heuristic value (lower is better) for each node:")
for node in graph:
    while True:
        try:
            h_val = float(input(f"Heuristic for {node}: "))
            h[node] = h_val
            break
        except ValueError:
            print("Please enter a valid number.")

# Input start and goal nodes
start_node = input("\nEnter the starting node: ").strip()
goal_node = input("Enter the goal node: ").strip()

# Simulated Annealing function
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
path, final_node = simulated_annealing(graph, start_node, goal_node, h)

print("\nPath taken:", path)
print("Final node:", final_node)