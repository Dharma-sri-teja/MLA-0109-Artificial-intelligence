# DFS implementation using adjacency list

# Represent the graph using a dictionary (adjacency list)
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [],
    8: []
}

# Depth-First Search function
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")   # Print visited node
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Source node to start DFS
print("DFS Traversal starting from node 5:")
dfs(graph, 5)
