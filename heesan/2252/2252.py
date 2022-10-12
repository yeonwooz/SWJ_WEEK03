# # topological sort
# 위상정렬은 순서가 정해져있는 작업을 차례로 수행해야 할 때
# 그 순서를 결정해주기 위해 사용하는 알고리즘입니다.
# 두 가지 해결책을 낸다는 특징이 있다.
# 1. 현재 그래프는 위상 정렬이 가능한지 !
# 2. 만약 위상정렬이 가능하다면 그 결과는 무엇인지 알려줌

# 하나는 스택을 이용한 방식, 다른 하나는 큐를 이용한 방식.
# 기본적으로 큐를 이용한 방식이 많이 사용됨

# N (학생들의 수) M (키를 비교한 횟수)

import sys
from collections import deque
input = sys.stdin.readline

# 노드의 갯수와 간선 갯수 입력받기
N, M = map(int, input().split())

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 (그래프) 초기화
graph = [[] for _ in range(N+1)]
# 모든 노드에 대한 진입차수는 초기화

indegree = [0] * (N+1)
# 방향 그래프의 모든 간선 정보를 입력 받는다.

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] = indegree[b] + 1


def topology_sort():
    result = []  # 수행 결과를 담을 리스트
    q = deque()
    # q는 출력 대기열

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] = indegree[i] - 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    for i in result: # 위상 정렬 수행 결과 출력
        print(i, end=" ")


# 먼저 넣은건 먼저 출력된다.
topology_sort()
