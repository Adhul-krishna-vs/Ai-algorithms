from sys import maxsize
from itertools import permutations

# Number of vertices in the graph
V = 4

# Implementation of the Traveling Salesman Problem
def travellingSalesmanProblem(graph, start):
    # Store all vertices except the starting vertex
    vertices = [i for i in range(V) if i != start]

    # Initialize minimum path weight to a large number
    min_path = maxsize
    best_path = None

    # Generate all possible permutations of vertices (excluding the starting vertex)
    for perm in permutations(vertices):
        # Initialize the current path weight
        current_pathweight = 0
        k = start

        # Calculate the weight of the current path
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        # Add the weight of returning to the starting vertex
        current_pathweight += graph[k][start]

        # Update the minimum path weight and best path if current is lower
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_path = (start,) + perm + (start,)

    # Return the minimum path cost and the corresponding path
    return min_path, best_path

# Driver Code
if __name__ == "__main__":
    # Matrix representation of the graph
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Starting point
    start = 0
    # Solve TSP
    min_path, best_path = travellingSalesmanProblem(graph, start)
    # Print the optimal path and minimum cost
    print("Optimal Path:", best_path)
    print("Minimum Path Cost:", min_path)
