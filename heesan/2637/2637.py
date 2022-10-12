# 장난감 만드는데 기본 부품과 중간 부품( 기본 부품으로 만듬 ) 이 필요함
# 기본 부품이 최소 단위 임
# ex)  1, 2, 3, 4 기본부품
# 중간부품 5 (1 두개 2 두개로 만들어짐)
# 중간부품 6 (중간5 2개, 기본3 3개 ,기본4 4개 )
# 장난감 완제품 7 (기본1 16개 , 기본2 16개, 기본3 9개, 기본4 17개)
# 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어져 있을 때,
# 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산하는 프로그램을 작성하시오.

# 기본 부품으로서 1, 2, 3, 4가 있다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 1부터 n-1까지는 기본,중간부품 번호 n은 완제품의 번호 ( 노드번호 )
m = int(input())  # 필요한 부품들 간의 관계가 3개의 자연수 x,y,k ( 간선 )
# x,y,k ==> 중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 y개 k개 필요하다.는 뜻이다.
# 두 중간 부품이 서로를 필요로 하는 경우가 없다.

# 노드별 연결 정보
graph = [[] for _ in range(n+1)]
# 가중치 입력 재료가 몇개 드는지?
matrix = [[0]*(n+1) for _ in range(n+1)]
# 진입 차수
indegree = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    indegree[a] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)


def topology_sort():
    print(q)  # deque([1, 2, 3, 4])
    '''
    q의 기능 :
    
    1.노드를 하나씩 pop하면서(now), pop된 노드의 목적지노드(v)가 가진 진입차수를 하나 낮춰줌(now -> v 간선 제거)

    2.필요행렬(matrix)에서 now행을 살펴보고,
    (= now를 만드는데 필요한 각노드와 그 개수를 살펴보고) 
    - if. now행의 모든 열이 0이라면, now를 만들기 위해 다른 노드가 필요없음. 즉 기본부품임. 
    - else. now 행의 어떤 열 i가 숫자면, now는 i라는 부품이 그 숫자만큼 존재해야 만들어질 수 있음. 즉 (i -> now 인데 i가 여러개 필요)

    이제 now가 생겼다. now -> next 니까, now를 가지고 next를 만들어보자!

    필요행렬(matrix)에서 next행을 살펴보고,
    - if. now행의 모든 열이 0이었다면, now는 이미 기본부품이라서, next 는 now가 needs개만 있으면 만들 수 있음.
    => matrix[next][now] 는 graph[now] 행의 needs 만큼 기록해주자.  

    - else. now 행의 어떤 열 i가 숫자였다면, now가 중간부품이다. i를 가지고 next를 만들기 위해서는 먼저 i로 now를 needs개 만들어야 한다.

    '''
    while q:
        now = q.popleft()  # now 1
        # next: now를 재료로 사용하는 부품. needs: now의 개수
        for next, needs in graph[now]:
            # 진입 차수 없는 노드(기본 부품)
            if matrix[now].count(0) == n+1:  # 기본부품이라면
                matrix[next][now] += needs
            else:
                for i in range(1, n+1):
                    # 중간부품 * 중간부품 필요 개수
                    matrix[next][i] += matrix[now][i] * needs
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)  # 진입차수 0개일시 큐에 추가


topology_sort()
print(matrix)
for i in enumerate(matrix[n]):
    if i[1] > 0:
        print(i[0], i[1])
