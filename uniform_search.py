import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue to store nodes with their costs
    priority_queue = [(0, start)]
    
    # Set to keep track of visited nodes
    visited = set()
    
    while priority_queue:
        # Pop the node with the lowest cost
        cost, current_node = heapq.heappop(priority_queue)
        
        # Check if the current node is the goal
        if current_node == goal:
            return cost
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                # Add the neighbor to the priority queue with the updated cost
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor))
    
    # If the goal is not reached, return an indication that the goal is unreachable
    return float('inf')

# Example usage:
# The graph is represented as an adjacency list with associated costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

result = uniform_cost_search(graph, start_node, goal_node)

if result == float('inf'):
    print(f"No path from {start_node} to {goal_node}")
else:
    print(f"Shortest path cost from {start_node} to {goal_node}: {result}")
