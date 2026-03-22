graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

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

# Run with depth limit = 2
dls(graph, 'A', 0, 2)