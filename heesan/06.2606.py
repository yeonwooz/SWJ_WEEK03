
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 마지막에 방문리스트를 순회하면서 True 면 count += 1

import sys
input = sys.stdin.readline

N = int(input())  # 정점 갯수
M = int(input())  # 간선 갯수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
count = 0


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


dfs(1)

for i in range(1, len(visited)):
    if visited[i] == True:
        count = count + 1


print(count-1)
