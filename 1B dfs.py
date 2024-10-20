graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'F'], 
    'D': ['B'], 
    'E': ['B', 'F'], 
    'F': ['C', 'E'] 
}

def dfs(graph,start):
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited
print("DFS",dfs(graph,'A'))
