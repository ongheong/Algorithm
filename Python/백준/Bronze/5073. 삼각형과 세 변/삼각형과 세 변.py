while True:
    triangle = list(map(int, input().split()))  
    if sum(triangle) == 0:
        break
    triangle.sort(reverse=True)

    if triangle[0] >= (triangle[1] + triangle[2]):
        print('Invalid')
        continue
    if triangle[0] == triangle[1] == triangle[2]:
        print('Equilateral')
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2]:
        print('Isosceles')
    else:
        print('Scalene')