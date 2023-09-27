import heapq

def bfs(start,goal,heuristic,graph):
    List=[(heuristic[start],start)]

    visited=set()

    Map={}
    while List:
        cost, node = heapq.heappop(List)

        if node is visited:
            continue

        visited.add(node)

        if node == goal:
            return construct_path(Map,goal)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(List,(heuristic[neighbor],neighbor))
                Map[neighbor]=node
    return []

def construct_path(Map,goal):
    path=[]

    current=goal
    while current:
        path.append(current)
        current=Map.get(current)
    return path[::-1]

graph={
    "A":{"B","C"},
    "B":{"D","E"},
    "C":{"F"},
    "D":{},
    "E":{},
    "F":{}
}

heuristic={
    "A":6,
    "B":4,
    "C":5,
    "D":2,
    "E":3,
    "F":1
}

start="A"
goal="D"

path=bfs(start,goal,heuristic,graph)

print(path)