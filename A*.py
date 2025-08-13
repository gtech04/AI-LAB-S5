import heapq
class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}
        self.parent = None
        self.g = float('inf')
    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
    def __lt__(self, other):
        return (self.g + self.heuristic) < (other.g + other.heuristic)
def a_star_search(start, goal):
    open_list = []
    closed_list = set()
    start.g = 0
    heapq.heappush(open_list, start)
    while open_list:
        current_node = heapq.heappop(open_list)
        print(f"Expanding node: {current_node.name}")
        if current_node == goal:
            return reconstruct_path(goal)
        closed_list.add(current_node)
        for neighbor, cost in current_node.neighbors.items():
            if neighbor in closed_list:
                continue
            tentative_g = current_node.g + cost
            if tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.parent = current_node
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)
    print("Goal node not found.")
    return None
def reconstruct_path(goal):
    path = []
    current = goal
    while current:
        path.append(current.name)
        current = current.parent
    path.reverse()
    return path
if __name__ == "__main__":
    a = Node('A', 5)
    b = Node('B', 3)
    c = Node('C', 1)
    d = Node('D', 2)
    e = Node('E', 0)
    a.add_neighbor(b, 1)
    a.add_neighbor(c, 4)
    b.add_neighbor(d, 2)
    c.add_neighbor(e, 3)
    d.add_neighbor(e, 1)
    path = a_star_search(a, e)
    if path:
        print("Path found:", " -> ".join(path))
