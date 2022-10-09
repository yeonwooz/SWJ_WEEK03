#started at 11:33
import sys
from collections import deque

def DFS(node, visited, N):
    if len(visited) == N:
        return
    for i in range(1, N + 1):
        if node != i and  arr[node][i] == 1 and i not in visited:
            visited.append(i)
            DFS(i, visited, N)

def BFS(node, visited):
    queue = deque()
    queue.append(node)
    visited.append(node)

    while queue:
        v = queue.popleft()
        for i in range(1, len(arr[v])):
            if v != i and arr[v][i] == 1 and i not in visited: 
                # visited 체크 필요할까? for문 진행방향상 필요 없을 것 같은데?
                visited.append(i) 
                queue.append(i)

N,M,V = map(int, sys.stdin.readline().split())
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

d_visited = [V]
DFS(V, d_visited , N)

b_visited = []
BFS(V, b_visited)
print(" ".join(str(s) for s in d_visited))
print(" ".join(str(s) for s in b_visited))

