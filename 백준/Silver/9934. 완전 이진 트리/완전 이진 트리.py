import sys
input = sys.stdin.readline

K = int(input().strip())
visit = list(map(int, input().split()))
result = [[] for _ in range(K)]

def makeTree(arr, x):
    root = (len(arr)//2) #/는 실수, //는 정수 몫 반환
    result[x].append(arr[root])
    if len(arr) == 1 : return
    makeTree(arr[:root], x+1) #mid 인덱스 앞의 원소들로 이루어진 배열과, 결과의 인덱스 들어감
    makeTree(arr[root+1:], x+1)


makeTree(visit, 0)
for i in range(K):
    print(*result[i]) #result는 이중리스트