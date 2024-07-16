import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())#왼쪽, 오른쪽 공백 삭제 

tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preOrder(root):
    if root != ".":
        print(root, end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root):
    if root != ".":
        inOrder(tree[root][0])
        print(root, end='')
        inOrder(tree[root][1])

def postOrder(root):
    if root != ".":
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')