import sys
input = sys.stdin.readline
import re

T = int(input())
rule = re.compile("^[A-F]?A+F+C+[A-F]?$")

for _ in range(T):
    str = input()
    if rule.match(str) != None: 
        print("Infected!")
        continue
    print("Good")
