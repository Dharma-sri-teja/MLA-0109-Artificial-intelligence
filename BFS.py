from collections import deque

# Represent the graph using adjacency list (dictionary)
graph = {
    0: [2, 3, 1],
    2: [4],
    3: [],
    1: [],
    4: []
}

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

# Starting node
print("BFS Traversal starting from node 0:")
bfs(graph, 0)
