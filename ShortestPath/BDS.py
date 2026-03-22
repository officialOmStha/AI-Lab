graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return True

    # Queues for both directions
    queue_start = deque([start])
    queue_goal = deque([goal])

    # Visited sets
    visited_start = {start}
    visited_goal = {goal}

    while queue_start and queue_goal:
        # Expand from start side
        if expand(graph, queue_start, visited_start, visited_goal):
            return True

        # Expand from goal side
        if expand(graph, queue_goal, visited_goal, visited_start):
            return True

    return False


def expand(graph, queue, visited_this_side, visited_other_side):
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor in visited_other_side:
            print(f"Meeting point: {neighbor}")
            return True

        if neighbor not in visited_this_side:
            visited_this_side.add(neighbor)
            queue.append(neighbor)

    return False


# Run
found = bidirectional_search(graph, 'A', 'F')
print("Path Exists:", found)