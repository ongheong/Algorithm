import sys
input =  sys.stdin.readline

N = int(input().strip())
solution = sorted(list(map(int, input().split(" "))))

start, end = 0, N-1
answer = abs(solution[start]+solution[end])
index = [solution[start], solution[end]]

while start < end: 
    left = solution[start]
    right = solution[end]
    sum = left+right
    
    if abs(sum) < answer:
        answer = abs(sum)
        index = [left, right]
        if answer == 0:
            break
    #0과 가깝게 만들기 위해서 start와 end를 한칸씩 당김
    if sum < 0:
        start += 1
        continue
    end -= 1

print(index[0], index[1])
