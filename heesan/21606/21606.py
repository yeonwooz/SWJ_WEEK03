# N개의 장소를 N-1개의 길이 있는 트리 형태로 단순화 시킨다.
# 트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.
# 시작점과 도착점을 정하고, 시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 지나지 않는 경로)를 따라 걷게 된다
# 트리 위의 두 점 사이의 거리는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.
# 일부 장소는 실내, 일부 장소는 실외
# 서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에, 산책의 시작점과 끝점은 모두 실내여야 한다.
# 산책 도중에 실내 장소를 만나면 그만두고자 하는 욕구 생김. 시작점과 끝점을 제외하고 실내 장소가 있으면 안됨.
# 서로 다른 산책 경로의 가짓 수를 구해라

# 입력
# 정점의 수 N
# 1과 0으로 이루어진 문자열 A . i번째 문자 A(i)가 1일 경우, i번 장소는 실내, 0인 경우 i번 장소는 실외
# 셋째 줄부터 N + 1번 줄까지는  i + 2번 줄에 트리의 각 간선을 나타내는 두 정수 ui,vi가 주어짐
# 이는 i번째 간선이 ui번 정점과 vi번 정점을 연결한다는 의미임.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# """문제 풀이 논리
# 1. 실외 점을 기준으로 인접해있는 실내 노드 개수를 count한다.
# 2. 실외 점을 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n * 1(중간 실외 점 선택) * (n-1) = n*(n-1)에 해당.
# 3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결할 때. 이를 분리해서 생각.
# """


def dfs(node, cnt):
    visited[node] = True

    for i in graph[node]:
        if located[i] == 1:
            cnt = cnt + 1
        elif not visited[i] and located[i] == 0:
            # 방문하지 않고 해당 i 점의 위치가 실외이면
            cnt = dfs(i, cnt)  # 해당 실외 점을 기준으로 dfs를 돈다
    return cnt


ans = 0
N = int(input())  # 정점 수 받기

# location 정보 받기: 앞에 0추가 함으로써 노드의 번호를 1부터 시작함.
located = [0] + list(map(int, input().strip()))

graph = [[] for _ in range(N+1)]  # 1번 노드부터 n번 까지 받아오기

for _ in range(N-1):  # 셋째 줄부터 n+1번 줄까지 받기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if located[a] == 1 and located[b] == 1:
        # 서로 방문하는 케이스 2가지라서 정답에 바로 추가하고 시작
        ans = ans + 2


sum = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i] and located[i] == 0:  # 실외인 애들 기준으로
        x = dfs(i, 0)  # 현재 cnt = 0
        sum = sum + x*(x-1) #실외인 노드를 기준으로 인접 노드 애들 개수 세는 게 총 n*(n-1)이니 실외 노드 걸릴 때마다 이걸 전부 세기

print(sum + ans)
