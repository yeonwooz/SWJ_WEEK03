from collections import deque
import sys
input = sys.stdin.readline


# 이동할 네 가지 방향 정의 ( 상, 하, 좌, 우)
# 방향 벡터 정의
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# N,M을 공백을 기준으로 구분하여 입력 받기
N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]


# 2차원 리스트의 맵 정보 입력 받기
visited = [[False] * M for _ in range(N)]
dq = deque()
dq.append((0, 0, 1))  # 출발점
visited[0][0] = True


def is_valid_coord(y, x): # 좌표가 이 행렬의 범위를 벗어나면 안됨.
    return 0 <= y < N and 0 <= x < M


while len(dq) > 0:  # 큐가 빌 때까지 실행.
    y, x, d = dq.popleft() # 튜플 그대로 pop함

    # 0,0이 출발점이니까 맨 끝 오른쪽 구석이 3,5 > 여기 도착했을 떄
    if y == N - 1 and x == M - 1:
        print(d)  # 이동한 칸수 출력
        break

    for k in range(4): # 조건에 맞는 4가지방향으로의 이동 
        ny = y + dy[k] 
        nx = x + dx[k] 
        nd = d + 1
        if is_valid_coord(ny, nx) and board[ny][nx] == "1" and not visited[ny][nx]:
            visited[ny][nx] = True
            dq.append((ny,nx,nd))