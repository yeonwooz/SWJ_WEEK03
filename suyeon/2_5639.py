#started at 10:20
#https://imzzan.tistory.com/41
import sys
sys.setrecursionlimit(10**6) #시스템 모듈에 있는 재귀 깊이를 늘려주는 함수

nums = []
while True:
    try:
        num = int(sys.stdin.readline())
        nums.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end + 1 # for문에서 모든 노드가 루트보다 작아서 mid가 안 정해질 경우를 대비해서 mid를 마지막 인덱스 + 1로 설정
    for i in range(first + 1, end + 1):
        if nums[first] < nums[i]:
            mid = i
            break
     
    # print(111)
    postorder(first+1, mid-1)
    # print(222)
    postorder(mid, end) 
    # print(333)
    print(nums[first]) # 재귀를 빠져나오면서 출력되므로 

postorder(0, len(nums) - 1)