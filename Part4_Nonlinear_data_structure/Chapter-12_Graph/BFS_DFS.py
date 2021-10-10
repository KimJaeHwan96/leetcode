"""
그래프 순회랑 그래프 탐색이라고도 불리우며 그래프의 각 정점을 방문하는 과정을 말한다.
그래프 순회에는 깊이 우선 탐색(Depth First Search) 와 너비 우선 탐색(Breadth First Search) 가 있다.

그래프를 표현하는 방벙으로 인접 행렬과 인접 리스트가 있다.
인접 행렬은 
graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
]
와 같이 표현하는 것이고 인접 리스트는 아래와 같이 표현한다.
"""
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


# DFS (재귀)
def recursive_dfs(vertex, discovered=[]):
    discovered.append(vertex)
    for w in graph[vertex]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


# DFS (스택)
def iterative_dfs(start_vertex):
    discovered = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in discovered:
            discovered.append(vertex)
            for w in graph[vertex]:
                stack.append(w)
    return discovered


# BFS (큐)
def iterative_bfs(start_vertex):
    discovered = [start_vertex]
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
