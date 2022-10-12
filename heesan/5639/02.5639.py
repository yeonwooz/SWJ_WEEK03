# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때,
# 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

# 입력
# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60

# 출력
# 5
# 28
# 24
# 45
# 30
# 60
# 52
# 98
# 50

# 전위 순회해서 트리 전체를 만들고 후위 순회하려니까 시간 초과가 발생함
# 트리로 만드는 코드 구현하자.(먼훗날 나에게...)



import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break
print(nums)  # [50,30,24,5,28,45,98,52,60]


def postorder(x, y):
    if x > y:
        return
    mid = y + 1  # 오른쪽 노드가 없을 경우

    for i in range(x+1, y+1): # x+1 인 이유는 50에서 시작하니까 50앞에는 원소가 
        # 없기 때문에 x+1 해준것이고 y+1을 한 이유는 마지막인덱스까지 순회하기위해 y+1을
        # 해준 것이다.
        if nums[x] < nums[i]: # 50 < 30 ..~~~~~ 
            mid = i # mid = 6
            break
    postorder(x+1, mid-1)    #mid -1 번째가 왼쪽의 마지막   
    # 왼쪽 확인 끝날때까지 재귀
    postorder(mid, y)  # 왼쪽 탐색 끝난 후 빠져나올 때의 mid      
    # y = 3 mid 4 가 처음으로 들어옴    # 오른쪽 확인 끝날떄까지 재귀
    print(nums[x])


postorder(0, len(nums)-1) # 0, 8

# 1 .recursion error가 발생해서 setrecursionlimit를 이용해서 재귀 깊이를 늘려줬다.
# 2. try~except를 이용해서 입력이 있을 때까지만 입력받음
# 3. 재귀 이용해서 가장 작은 트리부터 확인
# 4. for문을 돌려서 루트(nums[s])보다 커지면 오른쪽 노드!
# 왼쪽, 오른쪽 나뉘는 부분을 mid로 설정

# 5. [s+1, mid-1] 왼쪽 노드, [mid, e] 오른쪽 노드로 나누기
# -> 왼쪽 노드들만 다시 확인 (재귀) -> 가장 작은 트리까지!

# 6. 왼쪽 노드 출력하면 오른쪽 노드 확인하는 함수 확인
# -> 오른쪽 노드 출력
# -> 루트 출력
