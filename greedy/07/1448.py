# 삼각형 만들기
import sys

input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)
result = -1
for i in range(0, N - 2):
    if lst[i] < lst[i + 1] + lst[i + 2]:
        result = max(result, lst[i] + lst[i + 1] + lst[i + 2])
        break

print(result)

""" 삼각형 조건
a + b > c 
"""
