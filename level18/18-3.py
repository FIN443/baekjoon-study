from inspect import stack
import sys


input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    vps = input().rstrip()
    stack = []
    for i in vps:
        if stack and i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
    if stack:
        print("NO")
    else:
        print("YES")
