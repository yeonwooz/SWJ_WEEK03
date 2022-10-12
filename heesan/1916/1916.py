# 승덕님 설명
# 입력 에 5(도시 수) 8 ( 버스 수,간선 )
# 1번도시에서 출발함
# 1(시작) , 2(도착),  2(뵹)
# 힙큐 q = (0,1) 초기비용 0과 1은 시작 점(start) 초기 실행함수 파라미터의 인자


import sys
from heapq import heappush, heappop
import heapq
input = sys.stdin.readline
INF = int(1e9)

##### input #####
# city = node
# bus = line
city = int(input())
bus = int(input())

graph = [[] for _ in range(city+1)]
distance = [INF] * (city+1)

for _ in range(bus): 
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # (목적지, 최소비용)

start, end = map(int, input().split())

##### 함수 #####
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: 
        dist, now = heapq.heappop(q) # 힙이기 때문에 젤 작은값이 앞에 있음
        # 그게 pop이됨 
        if distance[now] < dist: # 이때까지 갱신된 비용 <  현재 now까지 쓴 비용.
            continue
        
        if now == end:
            return

        for i in graph[now]:  # i: A 목적지, 최소비용
            # 4번에서 갈수 있는 점들 => 5  :  (5, 3)
            cost = dist + i[1] # 비용을 더해진다. 
            if cost < distance[i[0]]: # 4 < 10 
                distance[i[0]] = cost # 작은 값으로 갱신 =>
                heapq.heappush(q, (cost, i[0]))


##### 메인 #####
dijkstra(start)
print(distance[end])
