def solve_csp_backtracking(graph, colors):
    def is_safe(node, color, assignment):
        for neighbor in graph.get(node, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(assignment):
        if len(assignment) == len(graph):
            return assignment
        unassigned_node = next((node for node in graph if node not in assignment), None)
        if unassigned_node is None:
            return None
        for color in colors:
            if is_safe(unassigned_node, color, assignment):
                assignment[unassigned_node] = color
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[unassigned_node]
        return None

    return backtrack({})


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D'],
}
colors = ['Red', 'Green', 'Blue']

solution = solve_csp_backtracking(graph, colors)

if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"Node {node}: Color {color}")
else:
    print("No solution found.")
