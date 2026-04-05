# Bidirectional Search Algorithm
# Searches from both start and goal nodes simultaneously to find a meeting point
# More efficient than BFS in undirected graphs for finding shortest path existence

from collections import deque

# Input the graph from user
graph = {}
num_nodes = int(input("Enter number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ").strip()
    neighbors_input = input(f"Enter neighbors of {node} separated by spaces: ").strip()
    neighbors = neighbors_input.split() if neighbors_input else []
    graph[node] = neighbors

# Expand function for one side
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

# Bidirectional Search function
def bidirectional_search(graph, start, goal):
    if start == goal:
        return True

    queue_start = deque([start])
    queue_goal = deque([goal])

    visited_start = {start}
    visited_goal = {goal}

    while queue_start and queue_goal:
        if expand(graph, queue_start, visited_start, visited_goal):
            return True
        if expand(graph, queue_goal, visited_goal, visited_start):
            return True

    return False

# User input for start and goal nodes
start_node = input("\nEnter the starting node: ").strip()
goal_node = input("Enter the goal node: ").strip()

# Run Bidirectional Search
found = bidirectional_search(graph, start_node, goal_node)
print("\nPath Exists:", found)