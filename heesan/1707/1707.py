# 어떻게 풀 것인가 ...

# 루트 기준 방문할 때 처음에 visitied = [0,0,0,0,0,~~~~,0]
# 처음 방문하고 걔에 대해서 루트로 다시 인접노드 방문하면 visitied 원소에 1을 할당해라.
# 또 걔에대해서 인접한노드를 방문하면은 원소 -1 을 할당해라
# 그러면 어떻게 1이랑 , 0을 할당할 것인가.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, state):
    global flag  # 이분그래프임
    visited[start] = state
    for i in graph[start]:
        if visited[i] == state:
            flag = 1
            return
        else:
            if not visited[i]:
                dfs(i, -state)


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    flag = 0

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V+1)

    for i in range(1, V+1):
        if not visited[i]:
            dfs(i, 1)

    if flag == 1:
        print("NO")
    else:
        print("YES")
