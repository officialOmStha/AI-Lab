graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dls(graph, node, target, depth, limit):
    if node == target:
        return True

    if depth == limit:
        return False

    for neighbor in graph[node]:
        if dls(graph, neighbor, target, depth + 1, limit):
            return True

    return False


def iddfs(graph, start, target, max_depth):
    for limit in range(max_depth + 1):
        print(f"\nDepth Limit: {limit}")
        if dls(graph, start, target, 0, limit):
            print("Target Found!")
            return True

    print("Target Not Found")
    return False


# Run IDS
iddfs(graph, 'A', 'F', 3)