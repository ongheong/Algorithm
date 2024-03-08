import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())# strip() : 왼쪽, 오른쪽 공백 삭제 

tree = {}#인덱스 값이 문자열로 들어가니까 dict가 편하다

for n in range(N):#해당 코드 주의하기
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

#전위/중위/후위순회는 순서를 기억할 것!
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