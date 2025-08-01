from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    predecessor = {start: None}

    while queue:
        current_node = queue.popleft()

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                predecessor[neighbor] = current_node

    path = []
    if goal in visited:
        current = goal
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        return path
    else:
        return "No path exists"

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'G': []
}

start = 'A'
goal = 'F'
path = bfs(graph, start, goal)
print("Path from start to goal:", path)
