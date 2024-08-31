n=int(input())
arr=list(map(int,input().split()))
b,c=map(int,input().split())
res=0
for i in range(n):
    arr[i]-=b
    res+=1
    if arr[i]>0:
        if arr[i]%c==0:
            res+=(arr[i]//c)
        else:
            res+=(arr[i]//c+1)

print(res)