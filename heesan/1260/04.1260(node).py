# 정점만 저장으로 해결
from collections import deque


def dfs(start):  # 시작 정점
    visited[start] = True  # 방문
    print(start, end=" ")  # 방문한 곳 출력

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# 여기부터 보자


def bfs(start): # 처음에 3이들어옴 
    queue = deque([start]) # 리스트말고 데크를 사용하겠다.
    visited[start] = True # 방문체크 
    while queue: # 처음 시작점을 방문체크 하면서 queue 에 담음
        # 현재정점이 pop 되면서 주변node가 큐에 삽입된다.
        out = queue.popleft()
        # 팝한 원소를 out에 할당하고 출력한다.
        print(out, end=" ")
        for i in graph[out]:
            if not visited[i]: 
                visited[i] = True
                queue.append(i)
    


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬

# print(graph)

for i in graph: # DFS 하기위해 반드시 정렬하는게 아니라 이 문제에서
    # 정점 번호가 작은 것을 먼저 방문하라고 했기 때문에 sort 하는 것이다. 
    i.sort() 

# print(graph)
# dfs

visited = [False] * (N + 1)
dfs(V)
print()

# bfs

visited = [False] * (N + 1)
bfs(V)
