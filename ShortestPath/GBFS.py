# Greedy Best-First Search (GBFS) Algorithm

import heapq

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
print("\nEnter heuristic value (estimated cost to goal) for each node:")
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

# Greedy Best-First Search function
def greedy_best_first(graph, start, goal, h):
    visited = set()
    priority_queue = []

    # Push the start node with its heuristic
    heapq.heappush(priority_queue, (h[start], start))

    while priority_queue:
        _, node = heapq.heappop(priority_queue)

        if node == goal:
            print("\nReached Goal:", node)
            return True

        if node not in visited:
            print("Visiting:", node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (h[neighbor], neighbor))

    print("\nGoal not reachable.")
    return False

# Run the algorithm
greedy_best_first(graph, start_node, goal_node, h)