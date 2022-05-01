# 이항계수 nCk -> n! / k!(n-k)!
from math import factorial

n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)

""" 동적계획법(dp)를 이용한 풀이
# nCk 파스칼의 삼각형
# https://blog.naver.com/vollollov/220947452823
n, k = map(int, input().split())
dp = [[0] * 1 for i in range(1001)]
dp[1].append(1)
for i in range(2, 1001):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[n + 1][k + 1] % 10007)
"""
