
# breadth first search using list and dictionaries
# only problem is to start with the node and go further
# BFS shortest path with levels

# tree_list = {
#             'A' : ['B','C','L'],
#             'B': ['D','E', 'A'],
#             'C' : ['F','G', 'A'],
#             'D' : ['B'],
#             'E' : ['B'],
#             'F' : ['C'],
#             'G' : ['C'],
#             'L' : ['A']
#             }


tree_list = {
            (0,'A') : [(1,'B'),(1,'C'),(1,'D')],
            (1,'B'): [(2,'E'), (2,'G'), (0,'A')],
            (1,'C') : [(2,'F'),(2,'H'), (0,'A')],
            (1,'D') : [(2,'I'), (2,'J'), (0,'A')],
            (2,'E') : [(1,'B'), (0,'A')],
            (2,'F') : [(1,'C'),  (0,'A')],
            (2,'G') : [(1,'B'), (0,'A')],
            (2,'H') : [(1,'C'), (0,'A')],
            (2,'I') : [(3,'G'), (1,'D')],
            (2,'J') : [(1,'D')],
            (3,'G') : [(2,'I')]
            }


start = input("Enter the start node and the level: ")
goal = input("Enter the goal node: ")

starting_node = tuple(map(str, start.split(',')))

visited = set()
queue = [[(int(starting_node[0]), starting_node[1])]]

if start[1] is goal:
    print(start)

else:
    while queue:
        
        path = queue.pop(0) 
        node = path[-1][1] #taking alphabets
        lev = path[-1][0] #taking level number
        
        if node not in visited:
            neighbours = tree_list[(lev, node)]

            for level,neighbour in neighbours:
                new_path = list(path)
                new_path.append((level,neighbour))
                queue.append(new_path)
            
                if neighbour == goal:
                    print(new_path)
                    exit(0)
            
            visited.add(node)
    
    print("No Path")










