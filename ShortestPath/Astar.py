# A* Search Algorithm (Graph Search with Heuristics)

import heapq

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors = []
    print(f"Enter neighbors and costs for {node} (format: neighbor cost), one per line. Type 'done' when finished:")
    while True:
        inp = input()
        if inp.lower() == 'done':
            break
        try:
            neighbor, cost = inp.split()
            neighbors.append((neighbor, float(cost)))
        except ValueError:
            print("Invalid input! Use format: neighbor cost (e.g., B 5)")
    graph[node] = neighbors

# Input heuristic values
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

# Reconstruct path from parent dictionary
def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]

# A* Search function
def a_star(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_cost = {start: 0}
    parent = {start: None}
    closed_list = set()

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(parent, current), g_cost[current]

        closed_list.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f = tentative_g + h[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None, float("inf")

# Run A* Search
path, cost = a_star(graph, start_node, goal_node, h)

print("\nShortest Path:", path)
print("Total Cost:", cost)