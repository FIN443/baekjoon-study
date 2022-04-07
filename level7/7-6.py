# 아파트는 0층부터있고 0층 i호에는 i명이 산다


def solution():
    K = int(input())
    N = int(input())
    result = [people for people in range(1, N + 1)]
    for i in range(K):
        for j in range(1, N):
            result[j] += result[j - 1]
    return result


T = int(input())
results = []
for _ in range(T):
    result = solution()
    results.append(result.pop())
print(*results, sep="\n")


# 0층 1호 [1]
# 0층 2호 [2]
# 0층 3호 -> [3]
# 1층 1호 [1]
# 1층 2호 [1+2]
# 1층 3호 -> 0층 1호 ~ 0층 3호 [1+2+3]
# 2층 1호 [1]
# 2층 2호 [1+(1+2)]
# 2층 3호 [1+(1+2)+(1+2+3)]
