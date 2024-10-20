graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
    }
def bfs(graph,start):
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print("BFS",bfs(graph,'A'))
