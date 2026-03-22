# Iterative Deepening DFS (IDDFS) Algorithm

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces (or leave blank if none): ").strip()
    neighbors = neighbors_input.split() if neighbors_input else []
    graph[node] = neighbors

# Depth-Limited Search function
def dls(graph, node, target, depth, limit):
    if node == target:
        return True
    if depth == limit:
        return False
    for neighbor in graph[node]:
        if dls(graph, neighbor, target, depth + 1, limit):
            return True
    return False

# Iterative Deepening DFS
def iddfs(graph, start, target, max_depth):
    for limit in range(max_depth + 1):
        print(f"\nDepth Limit: {limit}")
        if dls(graph, start, target, 0, limit):
            print("Target Found!")
            return True
    print("Target Not Found")
    return False

# User inputs
start_node = input("\nEnter the starting node: ").strip()
target_node = input("Enter the target node: ").strip()
max_depth = int(input("Enter the maximum depth to search: "))

# Run IDDFS
iddfs(graph, start_node, target_node, max_depth)