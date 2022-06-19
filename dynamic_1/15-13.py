N = int(input())
lst = [(0, 0)]
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x: x[0])

dp = [(0, 0)] + [0] * (N)

for i in range(1, N + 1):
    dp[i] = (lst[i][1], 1)
    for j in range(1, i):
        if lst[i][1] > dp[j][0] and dp[j][1] >= dp[i][1]:
            dp[i] = (lst[i][1], dp[j][1] + 1)

print(N - max(dp, key=lambda x: x[1])[1])
