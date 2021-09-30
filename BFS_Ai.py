BFS_graph = {
            'A': ['B', 'C', 'E'],
            'B': ['A','D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B'],
            'E': ['A', 'B','D'],
            'F': ['C'],
            'G': ['C']
         }

visited = []
queue = []

def bfs(visited, BFS_graph, node):
    visited.append(node)
    queue.append(node)



while queue:
    s = queue.pop(0)
    print (s, end = " ")
    for neighbour in BFS_graph[s]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)



bfs(visited, BFS_graph, 'A')