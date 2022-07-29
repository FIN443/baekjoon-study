N, K = map(int, input().split())

sum_n = K * (K + 1) // 2
if sum_n > N:
    print(-1)
elif (N - sum_n) % K == 0:
    print(K - 1)
else:
    print(K)
