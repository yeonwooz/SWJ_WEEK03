# 해당 문제는 DFS와 BFS의 기본개념을 이해하기 좋은문제이다. DFS는 재귀나 스택으로 구현하는게 보통이고 BFS는 queue로 구현하는게 보통이다.
#  또한 입력받은 노드의 개수만큼 이차원 리스트로(이차원 리스트의 인덱스:각 노드, 해당인덱스의 값들: 노드들과 연결 여부 False로 초기화한다음
# 만약 연결되어 있다면 True로 바꿔주는 형식으로 구현해도 되고 혹은 정점만 입력 받아서 그 정점만 찾아나가는 방식으로 구현해도 된다.

# 단, 정점만 찾아나가는 방식으로 구현할 경우 낮은 숫자부터 탐색하라고 되어있으니 오름차순 정렬이 필요하다.
#  queue는 리스트를 사용해도 되고 deque을 사용해도 되지만
# popleft가 구현되어 있는 시간복잡도가 더 낮은 deque을 사용하는 것이 좋다.


# True,False 로 구현

from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

# 인접행렬이란 배열의 인덱스 i,j가 서로 바뀌어도 같은 1의 값을 가진것
# 인접행렬을 통해 그래프가 양방향으로 연결됨을 표현할 수 있다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)


def bfs(V):
    q = deque([V])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다.
    # 리스트로 할 수도 있는데 큐를 쓸 수 있으면 사용하는게 낫다.
    # q: 현재 레벨에 속한 점들

    bfs_visited[V] = True  # 해당 V 값을 방문처리 = 현재 레벨중 하나를 방문함

    while q:  # q가 빌때까지 돈다.== 이 레벨의 정점들 중에 방문해야되는 점이 있다

        V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(V, end=" ")  # 해당 값 출력

        for i in range(1, N + 1):  # 1부터 N까지 돈다
            if not bfs_visited[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                bfs_visited[i] = True  # i 값을 방문처리


def dfs(V):
    dfs_visited[V] = True  # 해당 V값 방문처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not dfs_visited[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)


dfs(V)
bfs(V)


# 2.정점만 저장으로 해결


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
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
