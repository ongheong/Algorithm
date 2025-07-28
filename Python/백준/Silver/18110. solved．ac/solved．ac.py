import sys

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
else:
    arr = []
    
    for i in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))
        
    arr.sort()
    border = roundUp(n * 0.15)
    
    print(roundUp(sum(arr[border:n-border])/len(arr[border:n-border])))