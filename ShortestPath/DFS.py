#DFS (Depth-First Search) implementation with user input for graph.

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces (or leave blank if none): ").strip()
    neighbors = neighbors_input.split() if neighbors_input else []
    graph[node] = neighbors

# DFS function
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in graph:
        print(f"Error: node '{node}' does not exist in the graph.")
        return
    
    # Visit the node
    print(node, end=" ")
    visited.add(node)
    
    # Visit neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Ask user for starting node
start_node = input("Enter the starting node for DFS: ").strip()
print("\nDFS traversal:")
dfs(graph, start_node)