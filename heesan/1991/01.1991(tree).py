# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal),
# 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
# 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 전위 순회, 중위 순회, 후위 순회 함수를 작성하자
# DFS(깊이 우선 탐색)으로 작성할 수 있다.
# 전위, 중위, 후위 순회의 규칙에 따라 트리를 순회한다.

# 완전이진트리가 아니고, 문자열 기준으로 탐색을 진행해야 하므로 딕셔너리를 사용했다.

# 입력값
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

# 출력값
# ABDCEFG
# DBAECFG
# DBEGFCA
import sys
input = sys.stdin.readline

N = int(input())
tree = dict()

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]  # 처음 {'A': ['B', 'C']}



# root노드를 방문할 때 print를 해주면 경로를 찾을 수 있다.

def preorder(root):
    if root != '.':
        print(root, end='')  # root 를 방문할 때 출력해준다.
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


# 항상 A가 루트 노드가 된다.

preorder('A')
print()
inorder('A')
print()
postorder('A')
