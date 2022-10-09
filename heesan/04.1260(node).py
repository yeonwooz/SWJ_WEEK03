# 정점만 저장으로 해결
from collections import deque


def dfs(start):  # 시작 정점
    visited[start] = True  # 방문
    print(start, end=" ")  # 방문한 곳 출력

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# 여기부터 보자


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
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

for i in graph:
    i.sort()

# dfs

visited = [False] * (N + 1)
dfs(V)
print()

# bfs

visited = [False] * (N + 1)
bfs(V)
