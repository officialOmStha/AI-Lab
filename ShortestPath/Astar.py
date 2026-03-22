graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

import heapq

def a_star(graph, start, goal, h):
    # Priority queue: (f(n), node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start to node
    g_cost = {start: 0}

    # Parent tracking for path reconstruction
    parent = {start: None}

    # Visited nodes
    closed_list = set()

    while open_list:
        # Get node with lowest f(n)
        current_f, current = heapq.heappop(open_list)

        # Goal check
        if current == goal:
            return reconstruct_path(parent, current), g_cost[current]

        closed_list.add(current)

        # Explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_cost[current] + cost

            # If new path is better
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f = tentative_g + h[neighbor]

                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None, float("inf")


def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]

path, cost = a_star(graph, 'A', 'F', h)

print("Shortest Path:", path)
print("Total Cost:", cost)