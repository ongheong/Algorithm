import sys

N = int(sys.stdin.readline().strip())
files = {}

for n in range(N):
    name, extension = sys.stdin.readline().strip().split(".")
    if extension in files.keys():
        files[extension] += 1
    else:
        files[extension] = 1

#sorted 함수 쓰는 법 기억하기
#dict 자료구조 key, value 접근법 기억하기
sorted_files = sorted(files.items()) 

for key, value in sorted_files:
    print(key, value)