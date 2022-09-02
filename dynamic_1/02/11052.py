# 카드 구매하기
import sys


input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))


if N == 1:
    print(lst[0])
else:
    dp = [0 for _ in range(N + 1)]
    dp[1] = lst[0]
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + dp[j], lst[i - 1])
    print(dp[N])


"""
case 1
4
(1,1) (2,5) (3,6) (4,7)  
a1 = 1
a2 = 5
a3 = 6
a4 = 5+5
a5 = 5+6
a6 = (5+5)+5
a7 = (5+6)+5

case 2
(1,5) (2,10) (3,11) (4,12) (5,13) (6,30) (7,35) (8,40) (9,45) (10,47)
a1 = 5
a2 = 10
a3 = 15
a4 = 20
a5 = 25
a6 = 30
a7 = 35

case 3
12
(1,1) (2,1) (3,6) (4,8) (5,11) (6,1) (7,1) (8,1) (9,1) (10,1) (11,1) (12,1)
a1=1
a2=2
a3=6
a4=8
a5=11
a6=6+6
a7=6+8
a8=8+8
"""
