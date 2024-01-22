import heapq

def astar_search(graph, start, goal, heuristic):
    # Priority queue to store nodes with their estimated total cost
    priority_queue = [(0 + heuristic[start], 0, start)]
    
    # Set to keep track of visited nodes
    visited = set()
    
    while priority_queue:
        _, cost, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return cost
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                # Add the neighbor to the priority queue with the estimated total cost
                heapq.heappush(priority_queue, (cost + neighbor_cost + heuristic[neighbor], cost + neighbor_cost, neighbor))
    
    return float('inf')

# Example usage:
# The graph is represented as an adjacency list with associated costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic function (straight-line distance to the goal)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

result = astar_search(graph, start_node, goal_node, heuristic)

if result == float('inf'):
    print(f"No path from {start_node} to {goal_node}")
else:
    print(f"Shortest path cost from {start_node} to {goal_node} using A*: {result}")
