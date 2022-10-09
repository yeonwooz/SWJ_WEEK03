#started at 11:05
#https://hillier.tistory.com/54
import sys
V,E = map(int, sys.stdin.readline().split())

'''
1. kruskal : 두 간선의 루트를 재귀로 찾아가서 더 작은 루트로 모아준다

Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, sys.stdin.readline().split())))
Elist.sort(key=lambda x:x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s,e,w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        
        answer += w

print(answer)
'''

'''
#3.prim :
# '''

import heapq

visited = [False] * (V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0,1]]

for _ in range(E):
    s,e,w = map(int, sys.stdin.readline().split())
    Elist[s].append([w,e]) # 정점 s와 연결된 정점과 그 가중치
    Elist[e].append([w,s]) # 정점 e와 연결된 정점과 그 가중치

answer = 0
cnt = 0

while heap:
    if cnt == V:
        break
    w, node = heapq.heappop(heap)
    if not visited[node]:
        cnt += 1
        visited[node] = True
        answer += w

        for i in Elist[node]:
            heapq.heappush(heap, i)

print(answer)