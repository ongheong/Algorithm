n = int(input())
arr = []

def cntNum():
	if len(arr) == n:
		print(*arr)
		return
	for i in range(1, n+1):
		if i not in arr:
			arr.append(i)
			cntNum()
			arr.pop()

cntNum()