def dfs(cnt):
    global answer #global 변수 -> 해당 변수를 dfs 함수 내부에서 전역 스코프로 사용할 수 있게
    #키워드 없애면 외부의 answer값이 바뀌지 않
    if not cnt:
        tmp = int(''.join(nums))
        if answer < tmp:
            answer = tmp
        return
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            nums[i], nums[j] = nums[j], nums[i]
            tmp_key = ''.join(nums)
            if visited.get((tmp_key, cnt - 1), 1):
                visited[(tmp_key, cnt - 1)] = 0
                dfs(cnt-1)
            nums[i], nums[j] = nums[j], nums[i]

N = int(input())

for test_case in range(N):
    answer = -1
    n, c = input().split()
    nums = list(n)
    c = int(c)
    len_nums = len(nums)
    visited = {}
    dfs(c) #외부 함수에서 전역변수로 정의되어 nums, visited등의 변수 사용 가능. 단 dfs에서 값 변경해도 영향x
    print('#{} {}'.format(test_case+1, answer))
