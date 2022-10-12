
# 출력
# X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를 하나씩 오름차순으로 출력한다.
# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

# 입력
# N(도시갯수) , M(도로갯수) , K(거리정보) , X (출발 번호)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 모든 도로 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 양 방향이 아니라 단방향이라서 한쪽에만 담는다.


# 모든 도시에 대한 최단 거리 초기화
d = [-1] * (N+1) # 이 문제에서는 방문여부를 확인할 필요가 없다. 대신해서 이것을 사용한거다.
# 다돌았는데 -1 이남아있으면 거긴 못간 거다. 
d[X] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색 (BFS) 수해
q = deque([X])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if d[next_node] == -1:
            # 최단 거리 갱신
            d[next_node] = d[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, N+1):
    if d[i] == K:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
