def solution(brown, yellow):
    s = brown + yellow
    for w in range(s-1, 0, -1):
        if s%w != 0: continue
        h = s//w
        y = (w-2)*(h-2)
        b = s-y
        if y == yellow and b == brown:
            return [w, h]