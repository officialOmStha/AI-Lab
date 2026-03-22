# BFS Implementation in Python.
from collections import deque


# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces (or leave blank if none): ").strip()
    
    # Split neighbors, handle blank input
    if neighbors_input:
        neighbors = neighbors_input.split()
    else:
        neighbors = []
    
    graph[node] = neighbors

# BFS function
def bfs(graph, start):
    if start not in graph:
        print(f"Error: start node '{start}' does not exist in the graph.")
        return

    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Ask user for starting node
start_node = input("Enter the starting node for BFS: ").strip()
bfs(graph, start_node)