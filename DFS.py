def depth_first_search(graph, start_node, goal_node):
    open_list = [start_node]
    closed_list = set()
    path = {start_node: None}

    while open_list:
        current_node = open_list.pop()

        if current_node == goal_node:
            return reconstruct_path(path, start_node, goal_node)

        if current_node not in closed_list:
            closed_list.add(current_node)
            children = graph.get(current_node, [])

            for child in children:
                if child not in closed_list:
                    open_list.append(child)
                    path[child] = current_node

    return f"Goal node {goal_node} not found in the graph."

def reconstruct_path(path, start_node, goal_node):
    current_node = goal_node
    reversed_path = []

    while current_node is not None:
        reversed_path.append(current_node)
        current_node = path[current_node]

    return list(reversed(reversed_path))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'G': [],
}

start_node = 'A'
goal_node = 'F'
result = depth_first_search(graph, start_node, goal_node)
print("Path from start to goal:", result)
