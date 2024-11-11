from queue import heappop, heappush
from math import inf

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.heuristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost=1):
        self.edges.setdefault(node1, {})[node2] = cost
        if not self.directed:
            self.edges.setdefault(node2, {})[node1] = cost

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics

    def a_star_search(self, start, goal):
        fringe = [(self.heuristics.get(start, 0), start)]
        came_from = {start: None}
        cost_so_far = {start: 0}

        while fringe:
            _, current = heappop(fringe)
            if current == goal:
                return came_from, cost_so_far[goal]

            for neighbor, cost in self.edges.get(current, {}).items():
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current
                    heappush(fringe, (new_cost + self.heuristics.get(neighbor, inf), neighbor))
        return None, inf

    @staticmethod
    def print_path(came_from, goal):
        path = []
        while goal:
            path.append(goal)
            goal = came_from.get(goal)
        print(" -> ".join(reversed(path)))

# Create and set up the graph
graph = Graph(directed=True)
edges = [('A', 'B', 4), ('A', 'C', 1), ('B', 'D', 3), ('B', 'E', 8),
         ('C', 'D', 7), ('C', 'F', 6), ('D', 'C', 2), ('D', 'E', 4),
         ('E', 'G', 2), ('F', 'G', 8)]
for edge in edges:
    graph.add_edge(*edge)

graph.set_heuristics({'A': 8, 'B': 8, 'C': 6, 'D': 5, 'E': 1, 'F': 4, 'G': 0})

# Execute A* search
start, goal = 'A', 'G'
came_from, cost = graph.a_star_search(start, goal)

# Display the results
if came_from:
    print('Path:', end=' ')
    graph.print_path(came_from, goal)
    print('Cost:', cost)
