N = int(input())
lst = [0] + list(map(int, input().split()))
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)


for i in range(1, N + 1):
    dp1[i] = (lst[i], 1)
    for j in range(1, i):
        if lst[i] > dp1[j][0] and dp1[j][1] >= dp1[i][1]:
            dp1[i] = (lst[i], dp1[j][1] + 1)

lst = [0] + lst[::-1]
for i in range(1, N + 1):
    dp2[i] = (lst[i], 1)
    for j in range(1, i):
        if lst[i] > dp2[j][0] and dp2[j][1] >= dp2[i][1]:
            dp2[i] = (lst[i], dp2[j][1] + 1)

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp1[i][1] + dp2[-i][1] - 1
print(max(dp))
