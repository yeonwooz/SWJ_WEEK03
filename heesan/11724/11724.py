import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs_visited = [False] * (N+1)

count = 0


def dfs(start):
    global count
    dfs_visited[start] = True
    for i in graph[start]:
        if dfs_visited[i] == False:
            dfs(i)


for i in range(1, len(dfs_visited)):
    if dfs_visited[i] == False:
        dfs(i)
        count = count + 1

print(count)
