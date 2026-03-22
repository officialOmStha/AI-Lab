# Depth-Limited Search (DLS) Algorithm

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces (or leave blank if none): ").strip()
    neighbors = neighbors_input.split() if neighbors_input else []
    graph[node] = neighbors

# Depth-Limited Search function
def dls(graph, node, depth, limit, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")
    visited.add(node)

    # Stop if depth limit reached
    if depth == limit:
        return

    for neighbor in graph[node]:
        if neighbor not in visited:
            dls(graph, neighbor, depth + 1, limit, visited)

# User inputs
start_node = input("\nEnter the starting node: ").strip()
depth_limit = int(input("Enter the depth limit: "))

# Run DLS
print("\nDLS traversal:")
dls(graph, start_node, 0, depth_limit)