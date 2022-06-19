N, K = map(int, input().split())
lst = [[0, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = lst[i][0]
        v = lst[i][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])


""" 오답
N, K = map(int, input().split())
lst = [[0, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp = [[[0, 0] for _ in range(N + 1)] for i in range(N + 1)]


for i in range(1, N + 1):
    dp[i][i][0] = lst[i][0]
    dp[i][i][1] = lst[i][1]

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if dp[i][j - 1][0] + lst[j][0] <= K:
            dp[i][j][0] = dp[i][j - 1][0] + lst[j][0]
            dp[i][j][1] = dp[i][j - 1][1] + lst[j][1]
        else:
            dp[i][j][0] = dp[i][j - 1][0]
            dp[i][j][1] = dp[i][j - 1][1]

results = []
for i in dp:
    results.append(max(i))

print(max(results)[1])
"""
