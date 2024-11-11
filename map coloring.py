# Function to check if the current assignment of color to a region is safe (valid)
def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function to assign colors to the regions
def backtracking(assignment, graph, colors, regions):
    # If all regions are assigned a color, the assignment is complete
    if len(assignment) == len(regions):
        return assignment

    # Select an unassigned region
    region = next(region for region in regions if region not in assignment)

    # Try assigning each color to the selected region
    for color in colors:
        if is_safe(region, color, assignment, graph):
            # Assign the color to the region
            assignment[region] = color

            # Recursively try to assign colors to the remaining regions
            result = backtracking(assignment, graph, colors, regions)
            if result:
                return result

            # If assignment failed, backtrack by removing the color assignment
            del assignment[region]

    # If no color can be assigned to the current region, return None (backtrack)
    return None

# Function to solve the map coloring problem using backtracking
def map_coloring(graph, colors):
    # List of all regions in the graph
    regions = list(graph.keys())

    # Start with an empty assignment (no region has a color yet)
    assignment = {}

    # Call the backtracking function to find a valid assignment of colors
    return backtracking(assignment, graph, colors, regions)

# Example map: A simplified version of a country with regions as graph nodes
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C'],
}

# List of available colors
colors = ['Red', 'Green', 'Blue']

# Call the map coloring function
solution = map_coloring(graph, colors)

# Output the solution
if solution:
    print("Color assignment for the map:", solution)
else:
    print("No solution exists.")
