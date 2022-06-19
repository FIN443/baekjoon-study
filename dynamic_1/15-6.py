T = int(input())
lst = []
for _ in range(T):
    lst.append(list(map(int, input().split())))

dp = lst.pop()
for item in lst[::-1]:
    for i, num in enumerate(item):
        dp[i] = num + max(dp[i], dp[i + 1])

print(max(dp))
