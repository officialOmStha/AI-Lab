graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimated distance to goal F)
h = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

import heapq

def greedy_best_first(graph, start, goal, h):
    visited = set()
    priority_queue = []

    # (heuristic, node)
    heapq.heappush(priority_queue, (h[start], start))

    while priority_queue:
        _, node = heapq.heappop(priority_queue)

        if node == goal:
            print("Reached Goal:", node)
            return True

        if node not in visited:
            print("Visiting:", node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (h[neighbor], neighbor))

    return False


# Run
greedy_best_first(graph, 'A', 'F', h)